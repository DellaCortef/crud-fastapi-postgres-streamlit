from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from databases.database import Base


class ProductModel(Base):
    __tablename__ = "products"  # This will be the name of the table

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    category = Column(String, index=True)
    email_supplier = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)


# Export Base to make it accessible for metadata creation
__all__ = ["Base", "ProductModel"]
