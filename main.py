import functions_framework
from flask import request, jsonify
from google.cloud import bigquery
import datetime
import os
import re

# Set up BigQuery client
client = bigquery.Client()
dataset_id = 'orbit_ecommerce'
table_id = 'example_orders'
view_id = 'latest_orders'

@functions_framework.http
def handle_order(req):
    if req.method == 'POST':
        # Insert orders into BigQuery
        data = req.get_json()
        if data is None:
            return jsonify({"error": "Missing JSON body"}), 400
        if not isinstance(data, list):
            return jsonify({"error": "Input data should be a JSON array"}), 400
        if len(data) == 0:
            return jsonify({"error": "Input array is empty"}), 400
        if len(data) > 5000:
            return jsonify({"error": "Too many items in one request", "max_allowed": 5000}), 400

        required_fields = {"order_id", "order_date", "order_details", "order_status"}
        allowed_statuses = {"Processing", "Shipped", "Delivered"}
        id_pattern = re.compile(r'^[A-Za-z0-9_.\-]+$')

        validation_errors = []
        rows_to_insert = []
        for index, order in enumerate(data):
            item_errors = []
            if not isinstance(order, dict):
                validation_errors.append({"index": index, "errors": ["Item must be a JSON object"]})
                continue

            missing = required_fields - order.keys()
            if missing:
                item_errors.append(f"Missing required fields: {', '.join(sorted(missing))}")

            # Only run deeper checks if fields exist
            order_id = order.get("order_id")
            if order_id is None or not isinstance(order_id, str) or not order_id.strip():
                item_errors.append("order_id must be a non-empty string")
            elif len(order_id) > 64:
                item_errors.append("order_id is too long (max 64)")
            elif not id_pattern.match(order_id):
                item_errors.append("order_id contains invalid characters (allowed: letters, numbers, '_', '-', '.')")

            order_details = order.get("order_details")
            if order_details is None or not isinstance(order_details, str) or not order_details.strip():
                item_errors.append("order_details must be a non-empty string")
            elif len(order_details) > 256:
                item_errors.append("order_details is too long (max 256)")

            order_status = order.get("order_status")
            if order_status is None or not isinstance(order_status, str):
                item_errors.append("order_status must be a string")
            elif order_status not in allowed_statuses:
                item_errors.append(f"order_status must be one of {sorted(list(allowed_statuses))}")

            order_date = order.get("order_date")
            if order_date is None or not isinstance(order_date, str) or not order_date.strip():
                item_errors.append("order_date must be a non-empty ISO 8601 string (e.g., 2024-01-01T12:00:00Z)")
            else:
                # Basic ISO8601 validation (accepts trailing 'Z')
                try:
                    _ = datetime.datetime.fromisoformat(order_date.replace('Z', '+00:00'))
                except Exception:
                    item_errors.append("order_date must be a valid ISO 8601 timestamp (e.g., 2024-01-01T12:00:00Z)")

            if item_errors:
                validation_errors.append({"index": index, "order_id": order.get("order_id"), "errors": item_errors})
                continue

            rows_to_insert.append({
                'order_id': order_id,
                'order_date': order_date,
                'order_details': order_details,
                'order_status': order_status,
                'created_at': datetime.datetime.utcnow().isoformat() + "Z"
            })

        if validation_errors:
            return jsonify({"error": "Validation failed", "details": validation_errors}), 400

        table_ref = f"{client.project}.{dataset_id}.{table_id}"
        errors = client.insert_rows_json(table_ref, rows_to_insert)
        if errors:
            return jsonify({"error": "BigQuery insert failed", "details": errors}), 400
        return "Orders inserted successfully", 200

    elif req.method == 'GET':
        # Get latest orders from the existing view
        query = f"SELECT * FROM `{client.project}.{dataset_id}.{view_id}` ORDER BY order_id"
        
        try:
            results = client.query(query)
            latest_orders = [dict(row) for row in results]
            return jsonify(latest_orders)
        except Exception as e:
            # Log the error for debugging
            print(f"Error in GET request: {str(e)}")
            return jsonify({"error": f"Database query failed: {str(e)}"}), 500

    else:
        return "Method Not Allowed", 405