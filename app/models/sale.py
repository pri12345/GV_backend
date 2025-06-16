from app import db

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actual_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())
    total = db.Column(db.Float, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    suggested_price = db.Column(db.Float, nullable=False)
    price_deviation = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Sale {self.id} - Item {self.item_id}>' 