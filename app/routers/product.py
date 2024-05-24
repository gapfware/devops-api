from fastapi import APIRouter, Depends
from app.config.database import get_db
from app.controllers.product import ProductController
from app.schemas.product import ProductCreate, ProductUpdate, Product, ProductBase


router = APIRouter()


@router.get("/", response_model=list[Product])
async def get_all_products(db=Depends(get_db)):
    """
    Retrieve all products from the database.

    Parameters:
    - db: The database connection dependency.

    Returns:
    - A list of Product objects representing all the products in the database.
    """
    return ProductController(db).get_all()


@router.post("/", response_model=Product)
async def create_product(product: ProductCreate, db=Depends(get_db)):
    """
    Create a new product.

    Args:
        product (ProductCreate): The product data to be created.
        db: The database dependency.

    Returns:
        Product: The created product.
    """
    return ProductController(db).create(product)


@router.get("/{id}", response_model=Product)
async def get_product(id: int, db=Depends(get_db)):
    """
    Retrieve a product by its ID.

    Parameters:
    - id (int): The ID of the product to retrieve.
    - db: The database dependency.

    Returns:
    - Product: The retrieved product.
    """
    return ProductController(db).get_by_id(id)


@router.put("/{id}", response_model=Product)
async def update_product(id: int, product: ProductUpdate, db=Depends(get_db)):
    """
    Update a product with the given ID.

    Args:
        id (int): The ID of the product to update.
        product (ProductUpdate): The updated product data.
        db: The database dependency.

    Returns:
        Product: The updated product.

    """
    return ProductController(db).update(id, product)


@router.delete("/{id}", response_model=ProductBase)
async def delete_product(id: int, db=Depends(get_db)):
    """
    Delete a product by its ID.

    Parameters:
    - id (int): The ID of the product to be deleted.
    - db: The database dependency.

    Returns:
    - ProductBase: The deleted product.

    """
    return ProductController(db).delete(id)
