from app.models.rubro import Rubro
from app import db

class RubroService:
    @staticmethod
    def get_all_rubros():
        return Rubro.query.all()
    
    @staticmethod
    def get_rubro(rubro_id):
        return Rubro.query.get(rubro_id)
    
    @staticmethod
    def create_rubro(name, id, categorias):
        try:
            rubro = Rubro(
                name=name,
                id=id,
                categorias=categorias
            )
            
            db.session.add(rubro)
            db.session.commit()
            
            return rubro, None
        except Exception as e:
            db.session.rollback()
            return None, str(e) 