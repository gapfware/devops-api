from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    unique_name: str = Field(..., min_length=3, max_length=100)
    category_id: int = Field(1, gt=0)
    min_amount: int = Field(..., gt=0)
    existence: int = Field(..., ge=0)
    price_unit_usd: float = Field(..., gt=0)
    price_unit_pesos: float = Field(..., gt=0)
    description: str = Field(..., min_length=3, max_length=500)
    

class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int



