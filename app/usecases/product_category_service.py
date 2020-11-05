from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.product_category_repository import (
    ProductCategoryRepository as repository)
from app.schemas import product_category_schema as schema


class ProductCategoryService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return repository.reads(db, skip=skip, limit=limit)

    def read(db: Session, product_category_id: str):
        return repository.read(
            db,
            product_category_id=product_category_id)

    def create(
            db: Session,
            product_category: schema.ProductCategoryCreate):
        return repository.create(
            db=db,
            product_category=product_category)

    def update(
                db: Session,
                product_category: schema.ProductCategoryCreate,
                product_category_id: str
            ):
        return repository.update(
            db=db,
            product_category=product_category,
            product_category_id=product_category_id)

    def delete(db: Session, product_category_id: str):
        return repository.delete(
            db=db,
            product_category_id=product_category_id)
