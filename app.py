from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Sample orders data
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

@app.route('/')
def home():
    """Home page with order form and order list"""
    return render_template('home.html', orders=ORDERS)

@app.route('/add_order', methods=['POST'])
def add_order():
    """Add new order"""
    order_id = request.form.get('order_id')
    order_details = request.form.get('order_details')
    order_status = request.form.get('order_status')
    
    if not all([order_id, order_details, order_status]):
        flash('Please fill in all fields!', 'error')
        return redirect(url_for('home'))
    
    # Add new order to the list
    new_order = {
        'order_id': order_id,
        'order_details': order_details,
        'order_status': order_status
    }
    ORDERS.append(new_order)
    
    flash('Order added successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 