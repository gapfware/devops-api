from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from app.service.crud import crud_factory
from app.models import Product as ProductModel
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors
from app.controllers.category import CategoryController

DETAIL_NOT_FOUND = "Product not found"


class ProductController:
    def __init__(self, db):
        self.db = db
        self.crud = crud_factory(ProductModel)

    def get_all(self) -> JSONResponse:
        products = self.crud.get_all(db=self.db)
        return JSONResponse(content=products, status_code=status.HTTP_200_OK)

    def create(self, product) -> JSONResponse:
        category_exists = CategoryController(
            self.db).get_by_id(product.category_id)

        product_exists = self.crud.get_by_unique_name(
            db=self.db, unique_name=product.unique_name)

        if product_exists:
            raise HTTPException(
                status_code=400, detail="Product unique name already exists")
        product = self.crud.create(db=self.db, data=product)
        return JSONResponse(content=product, status_code=status.HTTP_201_CREATED)

    def get_by_id(self, id) -> JSONResponse:
        product = self.crud.get_by_id(db=self.db, id=id)
        if not product:
            raise HTTPException(
                status_code=404, detail=DETAIL_NOT_FOUND)
        return JSONResponse(content=product, status_code=status.HTTP_200_OK)

    def update(self, id, product) -> JSONResponse:
        product_exists = self.crud.get_by_id(db=self.db, id=id)
        if not product_exists:
            raise HTTPException(
                status_code=404, detail=DETAIL_NOT_FOUND)

        try:
            updated_product = self.crud.update(
                db=self.db, id=id, data=product)
        except Exception as e:
            raise HTTPException(
                status_code=400, detail="Product unique name already exists")

        return JSONResponse(content=updated_product, status_code=status.HTTP_200_OK)

    def delete(self, id) -> JSONResponse:
        product = self.crud.get_by_id(db=self.db, id=id)
        if not product:
            raise HTTPException(
                status_code=404, detail=DETAIL_NOT_FOUND)
        deleted_product = self.crud.delete(db=self.db, id=id)
        return JSONResponse(content=deleted_product, status_code=status.HTTP_200_OK)
