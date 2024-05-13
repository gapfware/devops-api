from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  index=True)
    unique_name = Column(String, unique=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
    min_amount = Column(Integer)
    existence = Column(Integer)
    price_unit_usd = Column(Float)
    price_unit_pesos = Column(Float)
    description = Column(Text)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    measures = Column(String)
    allows = Column(String)
    others = Column(JSON)

    products = relationship('Product', back_populates='category')
