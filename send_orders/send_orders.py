#!/usr/bin/env python3
"""
Python script to send all orders from orders_initial.json to your Cloud Function
Replace YOUR_FUNCTION_URL with your actual Cloud Function URL
"""

import json
import requests
import time
from typing import Dict, List

# Configuration
FUNCTION_URL = "YOUR_FUNCTION_URL"  # Replace with your actual function URL
ORDERS_FILE = "orders/orders_initial.json"

def send_orders():
    """Send all orders from the JSON file to the Cloud Function"""
    
    # Check if the orders file exists
    try:
        with open(ORDERS_FILE, 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        print(f"Error: Orders file not found: {ORDERS_FILE}")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {ORDERS_FILE}: {e}")
        return
    
    print(f"Found {len(orders)} orders to send")
    
    # Counters for tracking progress
    success_count = 0
    error_count = 0
    
    # Send each order
    for order in orders:
        try:
            # Send the order via POST request
            response = requests.post(
                FUNCTION_URL,
                headers={'Content-Type': 'application/json'},
                json=order,
                timeout=30
            )
            
            # Check if the request was successful
            if response.status_code in [200, 201]:
                print(f"✓ Sent order {order['order_id']}")
                success_count += 1
            else:
                print(f"✗ Failed to send order {order['order_id']} (HTTP {response.status_code})")
                error_count += 1
                
        except requests.exceptions.RequestException as e:
            print(f"✗ Error sending order {order['order_id']}: {e}")
            error_count += 1
        
        # Small delay to avoid overwhelming the server
        time.sleep(0.1)
    
    # Summary
    print(f"\n=== Summary ===")
    print(f"Successfully sent: {success_count} orders")
    print(f"Failed to send: {error_count} orders")
    print(f"Total processed: {success_count + error_count} orders")

if __name__ == "__main__":
    send_orders() 