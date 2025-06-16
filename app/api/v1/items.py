from flask import jsonify, render_template, request, redirect, url_for
from app.api.v1 import api_bp
from app.services.item_service import ItemService

@api_bp.route('/items', methods=['GET'])
def list_items():
    items = ItemService.get_all_items()
    return render_template('items.html', items=items)

@api_bp.route('/add_item', methods=['GET'])
def show_add_item_form():
    rubros = ItemService.get_all_rubros()
    suppliers = ItemService.get_all_suppliers()
    return render_template('add_item.html', rubros=rubros, suppliers=suppliers)

@api_bp.route('/add_item', methods=['POST'])
def add_item():
    try:
        # Get form data
        name = request.form.get('name')
        description = request.form.get('description')
        cost = float(request.form.get('cost'))
        price_once = float(request.form.get('price_once'))
        price_interior = float(request.form.get('price_interior'))
        quantity_per_bulto = int(request.form.get('quantity_per_bulto'))
        rubro_id = int(request.form.get('rubro_id'))
        supplier_id = int(request.form.get('supplier_id'))
        image_file = request.files.get('image')

        # Create item
        item, error = ItemService.create_item(
            name=name,
            description=description,
            cost=cost,
            price_once=price_once,
            price_interior=price_interior,
            quantity_per_bulto=quantity_per_bulto,
            rubro_id=rubro_id,
            supplier_id=supplier_id,
            image_file=image_file
        )

        if error:
            return render_template('add_item.html', error=error)

        return redirect(url_for('api.list_items'))

    except ValueError as e:
        return render_template('add_item.html', error="Invalid input values")
    except Exception as e:
        return render_template('add_item.html', error=str(e)) 