# PowerShell script to send all orders from orders_initial.json to your Cloud Function
# Replace YOUR_FUNCTION_URL with your actual Cloud Function URL

$FUNCTION_URL = "YOUR_FUNCTION_URL"  # Replace with your actual function URL
$ORDERS_FILE = "orders/orders_initial.json"

# Check if the orders file exists
if (-not (Test-Path $ORDERS_FILE)) {
    Write-Error "Orders file not found: $ORDERS_FILE"
    exit 1
}

# Read the JSON file
try {
    $orders = Get-Content $ORDERS_FILE | ConvertFrom-Json
    Write-Host "Found $($orders.Count) orders to send"
} catch {
    Write-Error "Failed to parse JSON file: $_"
    exit 1
}

# Counter for tracking progress
$successCount = 0
$errorCount = 0

# Send each order
foreach ($order in $orders) {
    try {
        # Convert the order to JSON string
        $orderJson = $order | ConvertTo-Json -Compress
        
        # Send the order via curl
        $response = curl -s -X POST $FUNCTION_URL `
            -H "Content-Type: application/json" `
            -d $orderJson
        
        # Check if the request was successful
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Sent order $($order.order_id)" -ForegroundColor Green
            $successCount++
        } else {
            Write-Host "✗ Failed to send order $($order.order_id)" -ForegroundColor Red
            $errorCount++
        }
        
        # Small delay to avoid overwhelming the server
        Start-Sleep -Milliseconds 100
        
    } catch {
        Write-Host "✗ Error sending order $($order.order_id): $_" -ForegroundColor Red
        $errorCount++
    }
}

# Summary
Write-Host "`n=== Summary ===" -ForegroundColor Yellow
Write-Host "Successfully sent: $successCount orders" -ForegroundColor Green
Write-Host "Failed to send: $errorCount orders" -ForegroundColor Red
Write-Host "Total processed: $($successCount + $errorCount) orders" 