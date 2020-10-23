from sqlalchemy.orm import Session
from app.repositories import product_detail_repository as repository
from app.schemas import product_detail_schema as schema


def get_product_details(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_product_details(db, skip=skip, limit=limit)


def get_product_detail(db: Session, product_detail_id: str):
    return repository.get_product_detail(
        db,
        product_detail_id=product_detail_id)


def create_user_product_detail(
        db: Session,
        product_detail: schema.ProductDetailCreate):
    return repository.create_user_product_detail(
        db=db,
        product_detail=product_detail)


def update_product_detail(
            db: Session,
            product_detail: schema.ProductDetailCreate,
            product_detail_id: str
        ):
    return repository.update_product_detail(
        db=db,
        product_detail=product_detail,
        product_detail_id=product_detail_id)


def delete_product_detail(db: Session, product_detail_id: str):
    return repository.delete_product_detail(
        db=db,
        product_detail_id=product_detail_id)
