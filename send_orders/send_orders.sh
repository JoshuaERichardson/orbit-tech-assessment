#!/bin/bash

# Bash script to send all orders from orders_initial.json to your Cloud Function
# Replace YOUR_FUNCTION_URL with your actual Cloud Function URL

FUNCTION_URL="YOUR_FUNCTION_URL"  # Replace with your actual function URL
ORDERS_FILE="orders/orders_initial.json"

# Check if the orders file exists
if [ ! -f "$ORDERS_FILE" ]; then
    echo "Error: Orders file not found: $ORDERS_FILE"
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed. Please install jq first."
    exit 1
fi

# Count total orders
TOTAL_ORDERS=$(jq length "$ORDERS_FILE")
echo "Found $TOTAL_ORDERS orders to send"

# Initialize counters
SUCCESS_COUNT=0
ERROR_COUNT=0

# Send each order
jq -c '.[]' "$ORDERS_FILE" | while read -r order; do
    # Extract order_id for logging
    ORDER_ID=$(echo "$order" | jq -r '.order_id')
    
    # Send the order via curl
    RESPONSE=$(curl -s -w "%{http_code}" -X POST "$FUNCTION_URL" \
        -H "Content-Type: application/json" \
        -d "$order")
    
    # Extract HTTP status code (last line of response)
    HTTP_CODE=$(echo "$RESPONSE" | tail -n1)
    RESPONSE_BODY=$(echo "$RESPONSE" | head -n -1)
    
    # Check if the request was successful (2xx status codes)
    if [[ $HTTP_CODE -ge 200 && $HTTP_CODE -lt 300 ]]; then
        echo "✓ Sent order $ORDER_ID"
        ((SUCCESS_COUNT++))
    else
        echo "✗ Failed to send order $ORDER_ID (HTTP $HTTP_CODE)"
        ((ERROR_COUNT++))
    fi
    
    # Small delay to avoid overwhelming the server
    sleep 0.1
done

# Summary
echo ""
echo "=== Summary ==="
echo "Successfully sent: $SUCCESS_COUNT orders"
echo "Failed to send: $ERROR_COUNT orders"
echo "Total processed: $((SUCCESS_COUNT + ERROR_COUNT)) orders" 