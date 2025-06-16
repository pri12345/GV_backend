# %%  Imports and initial configurations
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from models import db, Item, Sale, Stock_Addition  # Assuming models.py (in repo) contains the SQLAlchemy models

app = Flask(__name__)
CORS(app)

#%% Database configuration (later switch to PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#%% ROUTES

@app.route('/')   # Simple front-end to visualize
def home():
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Probando el backend con Flask"})

## Lists Item, Sales, Stock Added

@app.route('/items')
def list_items():
    items = Item.query.all()
    return render_template('items.html', items=items)

@app.route('/sales')
def list_sales():
    sales = Sale.query.all()
    return render_template('sales.html', sales=sales)

@app.route('/stock_additions')
def list_stock_additions():
    stock_additions = Stock_Addition.query.all()
    return render_template('stock_additions.html', stock_additions=stock_additions)

# ADD ITEM and RECORD SALE

@app.route('/add_item', methods=['GET'])
def show_add_item_form():
    return render_template('add_item.html')

@app.route('/add_item', methods=['POST'])
def add_item():
    id = request.form.get('id')  
    name = request.form['name']
    cost = float(request.form['cost'])
    price = float(request.form['price'])
    stock = int(request.form['stock'])
    new_item = Item(
                    id=id, name=name, cost=cost, price=price,
                    stock=stock       
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('list_items'))


@app.route('/record_sale', methods=['GET'])
def show_record_sale_form():
    return render_template('record_sale.html')

@app.route('/record_sale', methods=['POST'])
def record_sale():
    item_id = int(request.form['item_id'])
    quantity = int(request.form['quantity'])
    
    item = Item.query.get(item_id)
    if item and item.stock >= quantity:
        total = item.price * quantity
        new_sale = Sale(item_id=item_id, quantity=quantity, total=total)
        # Update the item's quantity
        item.stock -= quantity
        db.session.add(new_sale)
        db.session.commit()
        return redirect(url_for('list_sales'))
    else:
        return "Insufficient stock or item not found", 400
    

## ADD STOCK

@app.route('/add_stock', methods=['GET'])
def show_add_stock_form():
    return render_template('add_stock.html')

@app.route('/add_stock', methods=['POST'])
def add_stock():
    item_id = int(request.form['item_id'])
    additional_stock = int(request.form['additional_stock'])
    
    item = Item.query.get(item_id)
    if item:
        old_stock = item.stock
        movement = Stock_Addition(item_id=item_id, additional_stock=additional_stock)
        item.stock += additional_stock
        db.session.add(movement)
        db.session.commit()

        return (
                f"Succesfully added stock for item ID: {item_id}\n"
                f"name: {item.name}\n old stock: {old_stock}\n new stock: {item.stock}\n "
                f"movement number: {movement.id}\n movement timestamp: {movement.timestamp}"
            )
    
    else:
        return "Wrong Item ID, or inexistent Item", 400









# run
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
# %%
