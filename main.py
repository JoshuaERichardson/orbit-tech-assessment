import json
from flask import Flask, render_template, request, redirect, url_for, flash
import functions_framework

# Sample orders data (in a real app, this would be in a database)
ORDERS = [
    {
        'order_id': 'ORD-001',
        'order_details': 'Wireless Headphones - Qty: 2',
        'order_status': 'Shipped'
    },
    {
        'order_id': 'ORD-002', 
        'order_details': 'Smartphone - Qty: 1',
        'order_status': 'Processing'
    },
    {
        'order_id': 'ORD-003',
        'order_details': 'Running Shoes - Qty: 1',
        'order_status': 'Delivered'
    }
]

@functions_framework.http
def order_management(request):
    """HTTP Cloud Function for order management"""
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    if request.method == 'GET':
        # Return orders list as JSON
        return (json.dumps(ORDERS), 200, headers)
    
    elif request.method == 'POST':
        try:
            request_json = request.get_json()
            
            if not request_json:
                return (json.dumps({'error': 'No JSON data provided'}), 400, headers)
            
            order_id = request_json.get('order_id')
            order_details = request_json.get('order_details')
            order_status = request_json.get('order_status')
            
            if not all([order_id, order_details, order_status]):
                return (json.dumps({'error': 'Missing required fields'}), 400, headers)
            
            # Add new order
            new_order = {
                'order_id': order_id,
                'order_details': order_details,
                'order_status': order_status
            }
            ORDERS.append(new_order)
            
            return (json.dumps({'message': 'Order added successfully', 'order': new_order}), 201, headers)
            
        except Exception as e:
            return (json.dumps({'error': str(e)}), 500, headers)
    
    else:
        return (json.dumps({'error': 'Method not allowed'}), 405, headers) 