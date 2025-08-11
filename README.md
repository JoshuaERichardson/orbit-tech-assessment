# Orbit E-commerce Cloud Function

A Google Cloud Function that manages e-commerce orders with BigQuery integration. The function provides both POST (insert orders) and GET (retrieve latest order status) endpoints.

## Features

- **POST**: Insert multiple orders into BigQuery with automatic timestamping
- **GET**: Retrieve the latest status for each order ID from a pre-configured BigQuery view
- **BigQuery Integration**: Seamlessly works with Google Cloud BigQuery
- **Authentication**: Uses Google Cloud IAM for secure access

## Prerequisites

- Google Cloud Platform account
- Google Cloud CLI (`gcloud`) installed and configured
- Python 3.7+ (for local development)
- Access to BigQuery with the following resources:
  - Dataset: `orbit_ecommerce`
  - Table: `example_orders`
  - View: `latest_orders`


https://console.cloud.google.com/bigquery?ws=!1m5!1m4!4m3!1sorbit-example!2sorbit_ecommerce!3sexample_orders
## Deployment

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

(note: best to do within a venv)

### 2. Deploy to Google Cloud Functions

```bash
gcloud functions deploy orbit-example \
  --runtime python39 \
  --trigger-http \
  --allow-unauthenticated \
  --region us-west1 \
  --source . \
  --entry-point handle_order
```

**Note**: Replace `orbit-example` with your preferred function name and adjust the region as needed.

### 3. Set Environment Variables (if needed)

```bash
gcloud functions deploy orbit-example \
  --set-env-vars DATASET_ID=orbit_ecommerce,TABLE_ID=example_orders,VIEW_ID=latest_orders
```

## Testing

### 1. Test with Sample Data

First, test with a small dataset to ensure everything works:

```bash
# Create a test file
echo '[{"order_id": "TEST-001", "order_date": "2024-12-01T10:00:00Z", "order_details": "Test Product", "order_status": "Processing"}]' > test_orders.json

# POST test data
curl -X POST "https://orbit-example-989104885337.us-west1.run.app" \
  -H "Authorization: bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d @test_orders.json
```

### 2. Test GET Endpoint

```bash
curl -X GET "https://orbit-example-989104885337.us-west1.run.app" \
  -H "Authorization: bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json"
```

### 3. Load All Orders

Once testing is successful, load all orders:

```bash
curl -X POST "https://orbit-example-989104885337.us-west1.run.app" \
  -H "Authorization: bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d @orders/orders_update.json
```

(note: ensure to be cd'd into project root directory)

## API Endpoints

### POST / (Insert Orders)

**Purpose**: Insert new orders into BigQuery

**Request Body**: JSON array of order objects
```json
[
  {
    "order_id": "ORD-001",
    "order_date": "2024-12-01T10:00:00Z",
    "order_details": "Product Name",
    "order_status": "Processing"
  }
]
```

**Response**: 
- `200`: Orders inserted successfully
- `400`: Invalid input data or insertion errors

### GET / (Retrieve Latest Orders)

**Purpose**: Get the latest status for each order ID

**Response**: 
- `200`: JSON array of latest order statuses
- `500`: Database query errors

## BigQuery Schema

### Table: `example_orders`

| Field | Type | Description |
|-------|------|-------------|
| `order_id` | STRING | Unique order identifier |
| `order_date` | TIMESTAMP | When the order was placed |
| `order_details` | STRING | Product description |
| `order_status` | STRING | Order status (Processing/Shipped/Delivered) |
| `created_at` | TIMESTAMP | When the record was inserted |

### View: `latest_orders`

This view should contain the most recent entry for each `order_id` based on `created_at`.