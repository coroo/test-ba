from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import product_model as model
from app.schemas import product_schema as schema
from app.utils.uuid import generate_uuid


class ProductRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return db.query(
            model.Product
        ).offset(skip).limit(limit).all()

    def read(db: Session, product_id: str):
        return db.query(
            model.Product
        ).filter(model.Product.id == product_id).first()

    def create(db: Session, product: schema.ProductCreate):
        uuid = generate_uuid()
        db_product = model.Product(
            id=uuid,
            slug=product.slug,
            name=product.name,
            is_active=product.is_active,
            category_id=product.category_id,
            insurance_type_id=product.insurance_type_id,
            detail_id=product.detail_id,
            premium_type=product.premium_type,
            featured=product.featured,
            bundling_with_rider=product.bundling_with_rider)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    def update(
                db: Session,
                product: schema.ProductCreate,
                product_id: str
            ):
        db.query(
            model.Product
        ).filter(
            model.Product.id == product_id
        ).update({
            model.Product.slug: product.slug,
            model.Product.name: product.name,
            model.Product.is_active: product.is_active,
            model.Product.category_id: product.category_id,
            model.Product.insurance_type_id: product.insurance_type_id,
            model.Product.detail_id: product.detail_id,
            model.Product.premium_type: product.premium_type,
            model.Product.featured: product.featured,
            model.Product.bundling_with_rider: product.bundling_with_rider,
        })

        db.commit()
        return db.query(
            model.Product
        ).filter(model.Product.id == product_id).first()

    def delete(db: Session, product_id: int):
        db.query(
            model.Product
        ).filter(model.Product.id == product_id).delete()
        db.commit()
        return True
