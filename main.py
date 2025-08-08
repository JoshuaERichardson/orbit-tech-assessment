import functions_framework
from flask import request, jsonify
from google.cloud import bigquery
import datetime
import os

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
        if not isinstance(data, list):
            return "Input data should be a JSON array", 400
        rows_to_insert = []
        for order in data:
            # Add validation here as needed
            rows_to_insert.append({
                'order_id': order['order_id'],
                'order_date': order['order_date'],
                'order_details': order['order_details'],
                'order_status': order['order_status'],
                'created_at': bigquery.Timestamp(datetime.datetime.utcnow())
            })
        table_ref = f"{client.project}.{dataset_id}.{table_id}"
        errors = client.insert_rows_json(table_ref, rows_to_insert)
        if errors:
            return f"Errors: {errors}", 400
        return "Orders inserted successfully", 200

    elif req.method == 'GET':
        # Get latest orders
        query = f"SELECT latest_order.* FROM `{client.project}.{dataset_id}.{view_id}`"
        results = client.query(query)
        latest_orders = [dict(row) for row in results]
        return jsonify(latest_orders)

    else:
        return "Method Not Allowed", 405
