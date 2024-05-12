from fastapi import APIRouter, Depends
from config.database import get_db
from stock.models import Category as CategoryModel
from stock.schemas import CategoryCreate, CategoryUpdate, Category
from config.database import Base, engine

router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.get('/', response_model=list[Category])
async def get_categories(db=Depends(get_db)):
    return db.query(CategoryModel).all()


@router.post('/', response_model=Category)
async def create_category(category: CategoryCreate, db=Depends(get_db)):
    category = CategoryModel(**category.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
