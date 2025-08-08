import os
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure a resilient HTTP session for calling the Cloud Function
def _create_http_session() -> requests.Session:
    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods={"GET", "POST"},
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

http_session = _create_http_session()

# Cloud Function URL configured via environment variable
CLOUD_FUNCTION_URL = os.getenv('CLOUD_FUNCTION_URL', '').strip()

@app.route('/')
def home():
    """Home page with order form and order list (reads from Cloud Function)"""
    orders: list[dict] = []
    if not CLOUD_FUNCTION_URL:
        flash('Cloud Function URL is not configured. Set CLOUD_FUNCTION_URL env var.', 'error')
        return render_template('home.html', orders=orders)

    try:
        response = http_session.get(CLOUD_FUNCTION_URL, timeout=30)
        response.raise_for_status()
        orders = response.json()
    except Exception as exc:
        flash(f'Failed to load orders: {exc}', 'error')
    return render_template('home.html', orders=orders)

@app.route('/add_order', methods=['POST'])
def add_order():
    """Add new order"""
    order_id = request.form.get('order_id')
    order_details = request.form.get('order_details')
    order_status = request.form.get('order_status')
    
    if not all([order_id, order_details, order_status]):
        flash('Please fill in all fields!', 'error')
        return redirect(url_for('home'))
    
    if not CLOUD_FUNCTION_URL:
        flash('Cloud Function URL is not configured. Set CLOUD_FUNCTION_URL env var.', 'error')
        return redirect(url_for('home'))

    try:
        response = http_session.post(
            CLOUD_FUNCTION_URL,
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'order_id': order_id,
                'order_details': order_details,
                'order_status': order_status
            }),
            timeout=30,
        )
        response.raise_for_status()
        flash('Order added successfully!', 'success')
    except Exception as exc:
        flash(f'Failed to add order: {exc}', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True) 