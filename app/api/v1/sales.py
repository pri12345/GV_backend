from flask import jsonify, render_template, request, redirect, url_for
from app.api.v1 import api_bp
from app.models import Sale
from app.services.sale_service import SaleService

@api_bp.route('/sales', methods=['GET'])
def list_sales():
    sales = Sale.query.all()
    return render_template('sales.html', sales=sales)

@api_bp.route('/record_sale', methods=['GET'])
def show_record_sale_form():
    return render_template('record_sale.html')

@api_bp.route('/record_sale', methods=['POST'])
def record_sale():
    try:
        item_id = int(request.form['item_id'])
        quantity = int(request.form['quantity'])
        actual_price = float(request.form['actual_price'])
        
        sale, error = SaleService.record_sale(item_id, quantity, actual_price)
        
        if error:
            return error, 400
            
        return redirect(url_for('api.list_sales'))
        
    except ValueError:
        return "Invalid input values", 400 