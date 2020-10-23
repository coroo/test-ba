from sqlalchemy.orm import Session
from app.repositories import product_repository as repository
from app.schemas import product_schema as schema


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_products(db, skip=skip, limit=limit)


def get_product(db: Session, product_id: str):
    return repository.get_product(db, product_id=product_id)


def create_user_product(db: Session, product: schema.ProductCreate):
    return repository.create_user_product(db=db, product=product)


def update_product(
            db: Session,
            product: schema.ProductCreate,
            product_id: str
        ):
    return repository.update_product(
        db=db,
        product=product,
        product_id=product_id)


def delete_product(db: Session, product_id: str):
    return repository.delete_product(db=db, product_id=product_id)
