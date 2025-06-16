from app import db

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    condicion_iva = db.Column(db.String(50), nullable=False)  # Responsable Inscripto, Monotributista, etc.
    account_currency = db.Column(db.String(10), nullable=False)  # USD or ARS
    contact_info = db.Column(db.Text)
    address = db.Column(db.String(200))
    
    # Relationship with items
    items = db.relationship('Item', backref='supplier', lazy=True)
    
    def __repr__(self):
        return f'<Supplier {self.name}>' 