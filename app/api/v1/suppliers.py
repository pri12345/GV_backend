from flask import jsonify, render_template, request, redirect, url_for
from app.api.v1 import api_bp
from app.services.supplier_service import SupplierService

@api_bp.route('/suppliers', methods=['GET'])
def list_suppliers():
    suppliers = SupplierService.get_all_suppliers()
    return render_template('suppliers.html', suppliers=suppliers)

@api_bp.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    supplier = SupplierService.get_supplier(supplier_id)
    if supplier:
        return jsonify({
            'id': supplier.id,
            'name': supplier.name,
            'condicion_iva': supplier.condicion_iva,
            'account_currency': supplier.account_currency
        })
    return jsonify({'error': 'Supplier not found'}), 404

@api_bp.route('/suppliers/add', methods=['GET'])
def show_add_supplier_form():
    return render_template('add_supplier.html')

@api_bp.route('/suppliers/add', methods=['POST'])
def add_supplier():
    try:
        name = request.form.get('name')
        condicion_iva = request.form.get('condicion_iva')
        account_currency = request.form.get('account_currency')

        supplier, error = SupplierService.create_supplier(
            name=name,
            condicion_iva=condicion_iva,
            account_currency=account_currency
        )

        if error:
            return render_template('add_supplier.html', error=error)

        return redirect(url_for('api.list_suppliers'))

    except Exception as e:
        return render_template('add_supplier.html', error=str(e)) 