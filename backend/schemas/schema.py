from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional


class BaseCategory(Enum):
    category1 = "Electronic"
    category2 = "Household Appliance"
    category3 = "Furniture"
    category4 = "Clothes"
    category5 = "Shoes"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    category: str # Modified to str
    vendor_email: EmailStr

    @validator("category")
    def check_category(cls, v):
        if v in [item.value for item in CategoryBase]:
            return v
        raise ValueError("Invalid category")


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    supplier_email: Optional[EmailStr] = None

    @validator("category", pre=True, always=True)
    def check_category(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoryBase]:
            return v
        raise ValueError("Invalid category")