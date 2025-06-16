from app import db

class StockAddition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    additional_stock = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())
    
    def __repr__(self):
        return f'<StockAddition {self.id} - Item {self.item_id}>' 