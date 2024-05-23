from fastapi import APIRouter, Depends
from app.config.database import get_db
from app.controllers.product import ProductController
from app.schemas.product import ProductCreate, ProductUpdate, Product, ProductBase


router = APIRouter()


@router.get("/", response_model=list[Product])
async def get_all_products(db=Depends(get_db)):
    return ProductController(db).get_all()


@router.post("/", response_model=Product)
async def create_product(product: ProductCreate, db=Depends(get_db)):
    return ProductController(db).create(product)


@router.get("/{id}", response_model=Product)
async def get_product(id: int, db=Depends(get_db)):
    return ProductController(db).get_by_id(id)


@router.put("/{id}", response_model=Product)
async def update_product(id: int, product: ProductUpdate, db=Depends(get_db)):
    return ProductController(db).update(id, product)


@router.delete("/{id}", response_model=ProductBase)
async def delete_product(id: int, db=Depends(get_db)):
    return ProductController(db).delete(id)
