from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.product_detail_repository import (
    ProductDetailRepository as repository)
from app.schemas import product_detail_schema as schema


class ProductDetailService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return repository.reads(db, skip=skip, limit=limit)

    def read(db: Session, product_detail_id: str):
        return repository.read(
            db,
            product_detail_id=product_detail_id)

    def create(
            db: Session,
            product_detail: schema.ProductDetailCreate):
        return repository.create(
            db=db,
            product_detail=product_detail)

    def update(
                db: Session,
                product_detail: schema.ProductDetailCreate,
                product_detail_id: str
            ):
        return repository.update(
            db=db,
            product_detail=product_detail,
            product_detail_id=product_detail_id)

    def delete(db: Session, product_detail_id: str):
        return repository.delete(
            db=db,
            product_detail_id=product_detail_id)
