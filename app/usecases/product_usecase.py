from sqlalchemy.orm import Session
from app.repositories import product_repository
from app.schemas import product_schema


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return product_repository.get_products(db, skip=skip, limit=limit)


def get_product(db: Session, product_id: int):
    return product_repository.get_product(db, product_id=product_id)


def create_user_product(db: Session, product: product_schema.ItemCreate):
    return product_repository.create_user_product(db=db, product=product)
