# PowerShell script to send all orders from orders_update.json
# Make sure you're authenticated with gcloud first

$apiUrl = "https://orbit-example-989104885337.us-west1.run.app"
$ordersFile = "orders/orders_update.json"

# Get the identity token
Write-Host "Getting gcloud identity token..."
$token = gcloud auth print-identity-token
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to get gcloud identity token. Make sure you're authenticated."
    exit 1
}

# Read the orders file
Write-Host "Reading orders from $ordersFile..."
$orders = Get-Content $ordersFile -Raw

# Send the request
Write-Host "Sending orders to API..."
$headers = @{
    "Authorization" = "bearer $token"
    "Content-Type" = "application/json"
}

try {
    $response = Invoke-RestMethod -Uri $apiUrl -Method POST -Headers $headers -Body $orders
    Write-Host "Success! Response: $($response | ConvertTo-Json -Depth 10)"
} catch {
    Write-Error "Failed to send orders: $($_.Exception.Message)"
    if ($_.Exception.Response) {
        $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
        $responseBody = $reader.ReadToEnd()
        Write-Host "Response body: $responseBody"
    }
} 