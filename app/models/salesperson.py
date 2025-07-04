from app import db

class Salesperson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    commission_rate = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Salesperson {self.name}>' 