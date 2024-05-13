from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    measures: str
    allows: str
    others: Optional[dict] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True
