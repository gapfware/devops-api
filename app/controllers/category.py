from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from service.crud import crud_factory
from models import Category as CategoryModel

DETAIL_NOT_FOUND = "Category not found"


class CategoryController:
    def __init__(self, db):
        self.db = db
        self.crud = crud_factory(CategoryModel)

    def get_all(self) -> JSONResponse:
        categories = self.crud.get_all(db=self.db)
        return JSONResponse(content=categories, status_code=status.HTTP_200_OK)

    def create(self, category) -> JSONResponse:
        category_exists = self.crud.get_by_name(db=self.db, name=category.name)
        if category_exists:
            raise HTTPException(
                status_code=400, detail="Category already exists")
        category = self.crud.create(db=self.db, data=category)
        return JSONResponse(content=category, status_code=status.HTTP_201_CREATED)

    def get_by_id(self, id) -> JSONResponse:
        category = self.crud.get_by_id(db=self.db, id=id)
        if not category:
            raise HTTPException(
                status_code=404, detail=DETAIL_NOT_FOUND)
        return JSONResponse(content=category, status_code=status.HTTP_200_OK)

    def update(self, id, category) -> JSONResponse:
        category_exists = self.crud.get_by_id(db=self.db, id=id)
        if not category_exists:
            raise HTTPException(
                status_code=404, detail=DETAIL_NOT_FOUND)
        category_exists = self.crud.get_by_name(
            db=self.db, name=category.name)
        if category_exists:
            raise HTTPException(
                status_code=400, detail="Category already exists")
        updated_category = self.crud.update(db=self.db, id=id, data=category)
        return JSONResponse(content=updated_category, status_code=status.HTTP_200_OK)

    def delete(self, id) -> JSONResponse:
        category = self.crud.get_by_id(db=self.db, id=id)
        if not category:
            raise HTTPException(
                status_code=404, detail=DETAIL_NOT_FOUND)
        deleted_category = self.crud.delete(db=self.db, id=id)
        return JSONResponse(content=deleted_category, status_code=status.HTTP_200_OK)
