from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import product_detail_model as model
from app.schemas import product_detail_schema as schema
from app.utils.uuid import generate_uuid


class ProductDetailRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return db.query(
            model.ProductDetail
        ).offset(skip).limit(limit).all()

    def read(db: Session, product_detail_id: str):
        return db.query(
            model.ProductDetail
        ).filter(model.ProductDetail.id == product_detail_id).first()

    def create(
            db: Session,
            product_detail: schema.ProductDetailCreate):
        uuid = generate_uuid()
        db_product_detail = model.ProductDetail(
            id=uuid,
            summary=product_detail.summary,
            description=product_detail.description,
            icon=product_detail.icon,
            coverage_period=product_detail.coverage_period,)
        db.add(db_product_detail)
        db.commit()
        db.refresh(db_product_detail)
        return db_product_detail

    def update(
                db: Session,
                product_detail: schema.ProductDetailCreate,
                product_detail_id: str
            ):
        db.query(
            model.ProductDetail
        ).filter(
            model.ProductDetail.id == product_detail_id
        ).update({
            model.ProductDetail.summary: product_detail.summary,
            model.ProductDetail.description: product_detail.description,
            model.ProductDetail.icon: product_detail.icon,
            model.ProductDetail.coverage_period:
            product_detail.coverage_period,
        })

        db.commit()
        return db.query(
            model.ProductDetail
        ).filter(model.ProductDetail.id == product_detail_id).first()

    def delete(db: Session, product_detail_id: int):
        db.query(
            model.ProductDetail
        ).filter(model.ProductDetail.id == product_detail_id).delete()
        db.commit()
        return True
