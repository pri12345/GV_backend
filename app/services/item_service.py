from app.models.item import Item
from app.models.rubro import Rubro
from app.models.supplier import Supplier
from app.services.image_service import ImageService
from app import db

class ItemService:
    @staticmethod
    def get_all_items():
        return Item.query.all()
    
    @staticmethod
    def get_all_rubros():
        return Rubro.query.all()
    
    @staticmethod
    def get_all_suppliers():
        return Supplier.query.all()
    
    @staticmethod
    def create_item(name, description, cost, price_once, price_interior, 
                   quantity_per_bulto, rubro_id, supplier_id, image_file=None):
        try:
            # Create the item first to get an ID for the image
            item = Item(
                name=name,
                description=description,
                cost=cost,
                price_once=price_once,
                price_interior=price_interior,
                quantity_per_bulto=quantity_per_bulto,
                rubro_id=rubro_id,
                supplier_id=supplier_id
            )
            
            # Add to session to get the ID
            db.session.add(item)
            db.session.flush()
            
            # Handle image upload if provided
            if image_file:
                image_path = ImageService.save_image(image_file, item.id)
                if image_path:
                    item.image_path = image_path
            
            # Commit the transaction
            db.session.commit()
            return item, None
            
        except Exception as e:
            db.session.rollback()
            return None, str(e) 