from fastapi import APIRouter, Depends
from app.config.database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, Category
from app.controllers.category import CategoryController


router = APIRouter()


@router.get('/', response_model=list[Category])
async def get_categories(db=Depends(get_db)):
    """
    Retrieve all categories from the database.

    Parameters:
    - db: The database dependency.

    Returns:
    - A list of Category objects representing all categories in the database.
    """
    return CategoryController(db).get_all()


@router.post('/', response_model=Category)
async def create_category(category: CategoryCreate, db=Depends(get_db)):
    """
    Create a new category.

    Args:
        category (CategoryCreate): The category data to be created.
        db: The database dependency.
    Returns:
        Category: The created category.
    """
    return CategoryController(db).create(category)


@router.get('/{id}', response_model=Category)
async def get_category(id: int, db=Depends(get_db)):
    """
    Retrieve a category by its ID.

    Parameters:
    - id (int): The ID of the category to retrieve.
    - db (Database): The database connection.

    Returns:
    - Category: The retrieved category.

    Raises:
    - HTTPException: If the category with the given ID does not exist.
    """
    return CategoryController(db).get_by_id(id)


@router.put('/{id}', response_model=Category)
async def update_category(id: int, category: CategoryUpdate, db=Depends(get_db)):
    """
    Update a category with the given ID.

    Args:
        id (int): The ID of the category to update.
        category (CategoryUpdate): The updated category data.
        db: The database dependency.

    Returns:
        Category: The updated category.

    """
    return CategoryController(db).update(id, category)


@router.delete('/{id}', response_model=Category)
async def delete_category(id: int, db=Depends(get_db)):
    """
    Delete a category by its ID.

    Parameters:
    - id (int): The ID of the category to be deleted.
    - db: The database dependency.

    Returns:
    - Category: The deleted category.

    """
    return CategoryController(db).delete(id)
