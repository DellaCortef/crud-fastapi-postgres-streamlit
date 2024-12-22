from models.product import ProductModel
from databases.database import Base

# Explicitly list what should be imported when importing `models`
__all__ = ["Base", "ProductModel"]
