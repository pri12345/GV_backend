from app.models import StockAddition, Item, db
from sqlalchemy.exc import SQLAlchemyError

class StockService:
    @staticmethod
    def get_all_stock_additions() -> list[StockAddition]:
        """Get all stock additions from the database"""
        return StockAddition.query.all()
    
    @staticmethod
    def add_stock(item_id: int, additional_stock: int) -> tuple[StockAddition, str]:
        """
        Add stock to an item and record the addition.
        Returns a tuple of (stock_addition_object, error_message)
        """
        try:
            item = Item.query.get(item_id)
            
            if not item:
                return None, "Item not found"
            
            old_stock = item.stock
            movement = StockAddition(
                item_id=item_id,
                additional_stock=additional_stock
            )
            
            item.stock += additional_stock
            db.session.add(movement)
            db.session.commit()
            
            return movement, None
            
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return None, f"Unexpected error: {str(e)}" 