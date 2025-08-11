#!/usr/bin/env python3
"""
Python script to send all orders from orders_update.json to the API endpoint.
Make sure you're authenticated with gcloud first.
"""

import json
import subprocess
import requests
import sys

def get_gcloud_token():
    """Get the gcloud identity token."""
    try:
        result = subprocess.run(['gcloud', 'auth', 'print-identity-token'], 
                              capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Failed to get gcloud identity token: {e}")
        print("Make sure you're authenticated with gcloud auth login")
        sys.exit(1)

def send_orders():
    """Send all orders to the API."""
    api_url = "https://orbit-example-989104885337.us-west1.run.app"
    orders_file = "orders/orders_update.json"
    
    # Get the identity token
    print("Getting gcloud identity token...")
    token = get_gcloud_token()
    
    # Read the orders file
    print(f"Reading orders from {orders_file}...")
    try:
        with open(orders_file, 'r') as f:
            orders = json.load(f)
        print(f"Loaded {len(orders)} order entries")
    except FileNotFoundError:
        print(f"Error: {orders_file} not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {orders_file}: {e}")
        sys.exit(1)
    
    # Send the request
    print("Sending orders to API...")
    headers = {
        "Authorization": f"bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=orders)
        response.raise_for_status()
        print("Success!")
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send orders: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status: {e.response.status_code}")
            print(f"Response body: {e.response.text}")
        sys.exit(1)

if __name__ == "__main__":
    send_orders() 