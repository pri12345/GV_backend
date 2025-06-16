from app import db

class Rubro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    categorias = db.Column(db.Text)  # Short description of categories
    
    # Relationship with items
    items = db.relationship('Item', backref='rubro', lazy=True)
    
    def __repr__(self):
        return f'<Rubro {self.name}>' 