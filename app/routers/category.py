from fastapi import APIRouter, Depends
from app.config.database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, Category
from app.controllers.category import CategoryController


router = APIRouter()


@router.get('/', response_model=list[Category])
async def get_categories(db=Depends(get_db)):
    return CategoryController(db).get_all()


@router.post('/', response_model=Category)
async def create_category(category: CategoryCreate, db=Depends(get_db)):
    return CategoryController(db).create(category)


@router.get('/{id}', response_model=Category)
async def get_category(id: int, db=Depends(get_db)):
    return CategoryController(db).get_by_id(id)


@router.put('/{id}', response_model=Category)
async def update_category(id: int, category: CategoryUpdate, db=Depends(get_db)):
    return CategoryController(db).update(id, category)


@router.delete('/{id}', response_model=Category)
async def delete_category(id: int, db=Depends(get_db)):
    return CategoryController(db).delete(id)
