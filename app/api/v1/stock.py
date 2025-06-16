from flask import jsonify, render_template, request, redirect, url_for
from app.api.v1 import api_bp
from app.services.stock_service import StockService

@api_bp.route('/stock_additions', methods=['GET'])
def list_stock_additions():
    stock_additions = StockService.get_all_stock_additions()
    return render_template('stock_additions.html', stock_additions=stock_additions)

@api_bp.route('/add_stock', methods=['GET'])
def show_add_stock_form():
    return render_template('add_stock.html')

@api_bp.route('/add_stock', methods=['POST'])
def add_stock():
    try:
        item_id = int(request.form['item_id'])
        additional_stock = int(request.form['additional_stock'])
        
        movement, error = StockService.add_stock(item_id, additional_stock)
        
        if error:
            return error, 400
            
        return (
            f"Successfully added stock for item ID: {item_id}\n"
            f"name: {movement.item.name}\n old stock: {movement.item.stock - additional_stock}\n "
            f"new stock: {movement.item.stock}\n movement number: {movement.id}\n "
            f"movement timestamp: {movement.timestamp}"
        )
        
    except ValueError:
        return "Invalid input values", 400 