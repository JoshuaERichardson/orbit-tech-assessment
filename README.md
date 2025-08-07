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