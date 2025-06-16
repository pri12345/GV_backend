from app.models import Sale, Item, db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class SaleService:
    @staticmethod
    def record_sale(item_id: int, quantity: int, actual_price: float) -> tuple[Sale, str]:
        """
        Record a new sale and update stock levels.
        Returns a tuple of (sale_object, error_message)
        """
        try:
            item = Item.query.get(item_id)
            
            if not item:
                return None, "Item not found"
                
            if item.stock < quantity:
                return None, f"Insufficient stock. Only {item.stock} units available."
            
            # Calculate sale details
            suggested_price = item.price
            total = actual_price * quantity
            
            # Calculate price deviation as percentage
            price_deviation = ((actual_price - suggested_price) / suggested_price) * 100
            
            # Create sale record
            new_sale = Sale(
                item_id=item_id,
                quantity=quantity,
                actual_price=actual_price,
                suggested_price=suggested_price,
                price_deviation=price_deviation,
                total=total,
                timestamp=datetime.utcnow()
            )
            
            # Update stock
            item.stock -= quantity
            
            # Save changes
            db.session.add(new_sale)
            db.session.commit()
            
            return new_sale, None
            
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return None, str(e) 