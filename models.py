from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.String(200), nullable=True)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    sale_quantity = db.Column(db.Integer, nullable=False)
    sale_timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())
    total_sale_value = db.Column(db.Float, nullable=False)
