from app.models.supplier import Supplier
from app import db

class SupplierService:
    @staticmethod
    def get_all_suppliers():
        return Supplier.query.all()
    
    @staticmethod
    def get_supplier(supplier_id):
        return Supplier.query.get(supplier_id)
    
    @staticmethod
    def create_supplier(name, condicion_iva, account_currency):
        try:
            supplier = Supplier(
                name=name,
                condicion_iva=condicion_iva,
                account_currency=account_currency
            )
            
            db.session.add(supplier)
            db.session.commit()
            
            return supplier, None
        except Exception as e:
            db.session.rollback()
            return None, str(e) 