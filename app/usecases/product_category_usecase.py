from sqlalchemy.orm import Session
from app.repositories import product_category_repository as repository
from app.schemas import product_category_schema as schema


def get_product_categories(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_product_categories(db, skip=skip, limit=limit)


def get_product_category(db: Session, product_category_id: str):
    return repository.get_product_category(
        db,
        product_category_id=product_category_id)


def create_user_product_category(
        db: Session,
        product_category: schema.ProductCategoryCreate):
    return repository.create_user_product_category(
        db=db,
        product_category=product_category)


def update_product_category(
            db: Session,
            product_category: schema.ProductCategoryCreate,
            product_category_id: str
        ):
    return repository.update_product_category(
        db=db,
        product_category=product_category,
        product_category_id=product_category_id)


def delete_product_category(db: Session, product_category_id: str):
    return repository.delete_product_category(
        db=db,
        product_category_id=product_category_id)
