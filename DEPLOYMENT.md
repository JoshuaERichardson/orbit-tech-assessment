# Google Cloud Functions Deployment Guide

## Prerequisites
1. Install Google Cloud CLI: https://cloud.google.com/sdk/docs/install
2. Authenticate: `gcloud auth login`
3. Set your project: `gcloud config set project YOUR_PROJECT_ID`

## Deployment Steps

### Option 1: Deploy via gcloud CLI (No Dockerfile needed)
```bash
# Deploy the function
gcloud functions deploy order-management \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point handle_order
```

### Option 2: Deploy via Google Cloud Console
1. Go to Google Cloud Console → Cloud Functions
2. Click "Create Function"
3. Choose "HTTP" trigger
4. Set runtime to "Python 3.11"
5. Upload your `main.py` and `requirements.txt` files
6. Set entry point to `handle_order`

## Testing Your Function

### Get all orders:
```bash
curl -X GET https://YOUR_REGION-YOUR_PROJECT_ID.cloudfunctions.net/order-management
```

### Add new order:
```bash
curl -X POST https://YOUR_REGION-YOUR_PROJECT_ID.cloudfunctions.net/order-management \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "ORD-004",
    "order_details": "Laptop - Qty: 1",
    "order_status": "Processing"
  }'
```

## Important Notes
- **No Dockerfile required** for standard Python runtimes
- Function automatically scales based on traffic
- Pay only for actual execution time
- Cold starts may occur for first request after inactivity 