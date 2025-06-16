from app import db
from datetime import datetime

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    cost = db.Column(db.Float, nullable=False)  # Cost field
    price_once = db.Column(db.Float, nullable=False)  # Price for single unit
    price_interior = db.Column(db.Float, nullable=False)  # Price for interior/bulk
    quantity_per_bulto = db.Column(db.Integer, nullable=False)  # QxB
    stock = db.Column(db.Integer, default=0)
    image_path = db.Column(db.String(255))  # Path to stored image
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    rubro_id = db.Column(db.Integer, db.ForeignKey('rubro.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    
    # Relationships
    sales = db.relationship('Sale', backref='item', lazy=True)
    stock_additions = db.relationship('StockAddition', backref='item', lazy=True)
    
    def __repr__(self):
        return f'<Item {self.name}>' 