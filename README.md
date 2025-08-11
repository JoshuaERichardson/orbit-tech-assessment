# Simple Order Management System

A simple Flask application for managing orders with basic order tracking functionality.

## Features

- **Add Orders**: Simple form to add new orders with order ID, details, and status
- **Order List**: Display all orders in a clean table format
- **Status Tracking**: Track order status (Pending, Processing, Shipped, Delivered, Cancelled)
- **Responsive Design**: Clean, mobile-friendly interface using Bootstrap

## Form Fields

The application includes a simple form with three fields:
- **Order ID**: Unique identifier for the order
- **Order Details**: Description of the order contents
- **Order Status**: Current status of the order

## Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
tech_assessment/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    └── home.html         # Order form and list page
```

## Usage

- Fill out the form on the left side to add new orders
- View existing orders in the table on the right side
- Orders are stored in memory (resets when server restarts)

## Technical Details

- **Framework**: Flask 2.3.3
- **Frontend**: Bootstrap 5
- **Data Storage**: In-memory list (no database)
- **Responsive**: Mobile-friendly design

## Development

To run in development mode with auto-reload:
```bash
python app.py
```

The application will run on `http://localhost:5000` with debug mode enabled. 



SELF NOTES
curl -X POST https://us-central1-orbit-example.cloudfunctions.net/handle_order -H "Content-Type: application/json" -d @orders.json

curl -X POST "https://handle-order-989104885337.us-central1.run.app" \
-H "Content-Type: application/json" \
-d '[
    {
      "order_id": "12345",
      "order_date": "2024-05-01T10:00:00Z",
      "order_details": "Item A, Item B",
      "order_status": "Shipped"
    },
    {
      "order_id": "12346",
      "order_date": "2024-05-01T11:00:00Z",
      "order_details": "Item C, Item D",
      "order_status": "Processing"
    }
  ]'

  curl -X POST "https://orbit-tech-assessment-989104885337.us-west1.run.app" \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '[
  {"order_id": "ORD-001", "order_date": "2025-08-01T10:00:00Z", "order_details": "Leaky Shoes", "order_status": "Processing"},
  {"order_id": "ORD-002", "order_date": "2025-08-01T10:15:00Z", "order_details": "Moist Mittens", "order_status": "Shipped"},
  {"order_id": "ORD-003", "order_date": "2025-08-01T10:30:00Z", "order_details": "Soggy Socks", "order_status": "Delivered"},
  {"order_id": "ORD-004", "order_date": "2025-08-01T10:45:00Z", "order_details": "Humid Hoodie", "order_status": "Processing"},
  {"order_id": "ORD-005", "order_date": "2025-08-01T11:00:00Z", "order_details": "Sopping Sneakers", "order_status": "Shipped"},
  {"order_id": "ORD-006", "order_date": "2025-08-01T11:15:00Z", "order_details": "Waterlogged Wallet", "order_status": "Delivered"},
  {"order_id": "ORD-007", "order_date": "2025-08-01T11:30:00Z", "order_details": "Pre-Rained Raincoat", "order_status": "Processing"},
  {"order_id": "ORD-008", "order_date": "2025-08-01T11:45:00Z", "order_details": "Dewy Denim", "order_status": "Shipped"},
  {"order_id": "ORD-009", "order_date": "2025-08-01T12:00:00Z", "order_details": "Flooded Fleece", "order_status": "Delivered"},
  {"order_id": "ORD-010", "order_date": "2025-08-01T12:15:00Z", "order_details": "Sorta Short Shorts", "order_status": "Processing"},
  {"order_id": "ORD-011", "order_date": "2025-08-01T12:30:00Z", "order_details": "Leaky Shoes", "order_status": "Shipped"},
  {"order_id": "ORD-012", "order_date": "2025-08-01T12:45:00Z", "order_details": "Moist Mittens", "order_status": "Delivered"},
  {"order_id": "ORD-013", "order_date": "2025-08-01T13:00:00Z", "order_details": "Soggy Socks", "order_status": "Processing"},
  {"order_id": "ORD-014", "order_date": "2025-08-01T13:15:00Z", "order_details": "Humid Hoodie", "order_status": "Shipped"},
  {"order_id": "ORD-015", "order_date": "2025-08-01T13:30:00Z", "order_details": "Sopping Sneakers", "order_status": "Delivered"},
  {"order_id": "ORD-016", "order_date": "2025-08-01T13:45:00Z", "order_details": "Waterlogged Wallet", "order_status": "Processing"},
  {"order_id": "ORD-017", "order_date": "2025-08-01T14:00:00Z", "order_details": "Pre-Rained Raincoat", "order_status": "Shipped"},
  {"order_id": "ORD-018", "order_date": "2025-08-01T14:15:00Z", "order_details": "Dewy Denim", "order_status": "Delivered"},
  {"order_id": "ORD-019", "order_date": "2025-08-01T14:30:00Z", "order_details": "Flooded Fleece", "order_status": "Processing"},
  {"order_id": "ORD-020", "order_date": "2025-08-01T14:45:00Z", "order_details": "Sorta Short Shorts", "order_status": "Shipped"},
  {"order_id": "ORD-021", "order_date": "2025-08-01T15:00:00Z", "order_details": "Leaky Shoes", "order_status": "Delivered"},
  {"order_id": "ORD-022", "order_date": "2025-08-01T15:15:00Z", "order_details": "Moist Mittens", "order_status": "Processing"},
  {"order_id": "ORD-023", "order_date": "2025-08-01T15:30:00Z", "order_details": "Soggy Socks", "order_status": "Shipped"},
  {"order_id": "ORD-024", "order_date": "2025-08-01T15:45:00Z", "order_details": "Humid Hoodie", "order_status": "Delivered"},
  {"order_id": "ORD-025", "order_date": "2025-08-01T16:00:00Z", "order_details": "Sopping Sneakers", "order_status": "Processing"},
  {"order_id": "ORD-026", "order_date": "2025-08-01T16:15:00Z", "order_details": "Waterlogged Wallet", "order_status": "Shipped"},
  {"order_id": "ORD-027", "order_date": "2025-08-01T16:30:00Z", "order_details": "Pre-Rained Raincoat", "order_status": "Delivered"},
  {"order_id": "ORD-028", "order_date": "2025-08-01T16:45:00Z", "order_details": "Dewy Denim", "order_status": "Processing"},
  {"order_id": "ORD-029", "order_date": "2025-08-01T17:00:00Z", "order_details": "Flooded Fleece", "order_status": "Shipped"},
  {"order_id": "ORD-030", "order_date": "2025-08-01T17:15:00Z", "order_details": "Sorta Short Shorts", "order_status": "Delivered"},
  {"order_id": "ORD-031", "order_date": "2025-08-01T17:30:00Z", "order_details": "Leaky Shoes", "order_status": "Processing"},
  {"order_id": "ORD-032", "order_date": "2025-08-01T17:45:00Z", "order_details": "Moist Mittens", "order_status": "Shipped"},
  {"order_id": "ORD-033", "order_date": "2025-08-01T18:00:00Z", "order_details": "Soggy Socks", "order_status": "Delivered"},
  {"order_id": "ORD-034", "order_date": "2025-08-01T18:15:00Z", "order_details": "Humid Hoodie", "order_status": "Processing"},
  {"order_id": "ORD-035", "order_date": "2025-08-01T18:30:00Z", "order_details": "Sopping Sneakers", "order_status": "Shipped"},
  {"order_id": "ORD-036", "order_date": "2025-08-01T18:45:00Z", "order_details": "Waterlogged Wallet", "order_status": "Delivered"},
  {"order_id": "ORD-037", "order_date": "2025-08-01T19:00:00Z", "order_details": "Pre-Rained Raincoat", "order_status": "Processing"},
  {"order_id": "ORD-038", "order_date": "2025-08-01T19:15:00Z", "order_details": "Dewy Denim", "order_status": "Shipped"},
  {"order_id": "ORD-039", "order_date": "2025-08-01T19:30:00Z", "order_details": "Flooded Fleece", "order_status": "Delivered"},
  {"order_id": "ORD-040", "order_date": "2025-08-01T19:45:00Z", "order_details": "Sorta Short Shorts", "order_status": "Processing"},
  {"order_id": "ORD-041", "order_date": "2025-08-01T20:00:00Z", "order_details": "Leaky Shoes", "order_status": "Shipped"},
  {"order_id": "ORD-042", "order_date": "2025-08-01T20:15:00Z", "order_details": "Moist Mittens", "order_status": "Delivered"},
  {"order_id": "ORD-043", "order_date": "2025-08-01T20:30:00Z", "order_details": "Soggy Socks", "order_status": "Processing"},
  {"order_id": "ORD-044", "order_date": "2025-08-01T20:45:00Z", "order_details": "Humid Hoodie", "order_status": "Shipped"},
  {"order_id": "ORD-045", "order_date": "2025-08-01T21:00:00Z", "order_details": "Sopping Sneakers", "order_status": "Delivered"},
  {"order_id": "ORD-046", "order_date": "2025-08-01T21:15:00Z", "order_details": "Waterlogged Wallet", "order_status": "Processing"},
  {"order_id": "ORD-047", "order_date": "2025-08-01T21:30:00Z", "order_details": "Pre-Rained Raincoat", "order_status": "Shipped"},
  {"order_id": "ORD-048", "order_date": "2025-08-01T21:45:00Z", "order_details": "Dewy Denim", "order_status": "Delivered"},
  {"order_id": "ORD-049", "order_date": "2025-08-01T22:00:00Z", "order_details": "Flooded Fleece", "order_status": "Processing"},
  {"order_id": "ORD-050", "order_date": "2025-08-01T22:15:00Z", "order_details": "Sorta Short Shorts", "order_status": "Shipped"}
]
  '


  curl -X POST "https://orbit-example-989104885337.us-west1.run.app" \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '[{"order_id": "ORD-001", "order_date": "2025-08-01T10:00:00Z", "order_details": "Leaky Shoes", "order_status": "Delivered"},
  {"order_id": "ORD-002", "order_date": "2025-09-01T10:15:00Z", "order_details": "Moist Mittens", "order_status": "Delivered"},
  {"order_id": "ORD-003", "order_date": "2025-09-01T10:30:00Z", "order_details": "Soggy Socks", "order_status": "Delivered"},
  {"order_id": "ORD-004", "order_date": "2025-09-01T10:45:00Z", "order_details": "Humid Hoodie", "order_status": "Delivered"},
  {"order_id": "ORD-005", "order_date": "2025-09-01T11:00:00Z", "order_details": "Sopping Sneakers", "order_status": "Delivered"},
  {"order_id": "ORD-006", "order_date": "2025-09-01T11:15:00Z", "order_details": "Waterlogged Wallet", "order_status": "Delivered"},
  {"order_id": "ORD-007", "order_date": "2025-08-01T11:30:00Z", "order_details": "Pre-Rained Raincoat", "order_status": "Delivered"},
  {"order_id": "ORD-008", "order_date": "2025-08-01T11:45:00Z", "order_details": "Dewy Denim", "order_status": "Delivered"},
  {"order_id": "ORD-009", "order_date": "2025-08-01T12:00:00Z", "order_details": "Flooded Fleece", "order_status": "Delivered"},
  {"order_id": "ORD-010", "order_date": "2025-08-01T12:15:00Z", "order_details": "Sorta Short Shorts", "order_status": "Delivered"}
]'