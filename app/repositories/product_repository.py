from sqlalchemy.orm import Session

from app.models import product_model
from app.schemas import product_schema
from app.utils.uuid import generate_uuid


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(
        product_model.Product
    ).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: str):
    return db.query(
        product_model.Product
    ).filter(product_model.Product.id == product_id).first()


def create_user_product(db: Session, product: product_schema.ProductCreate):
    uuid = generate_uuid()
    db_product = product_model.Product(
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


def update_product(
            db: Session,
            product: product_schema.ProductCreate,
            product_id: str
        ):
    db.query(
        product_model.Product
    ).filter(
        product_model.Product.id == product_id
    ).update({
        product_model.Product.slug: product.slug,
        product_model.Product.name: product.name,
        product_model.Product.is_active: product.is_active,
        product_model.Product.category_id: product.category_id,
        product_model.Product.insurance_type_id: product.insurance_type_id,
        product_model.Product.detail_id: product.detail_id,
        product_model.Product.premium_type: product.premium_type,
        product_model.Product.featured: product.featured,
        product_model.Product.bundling_with_rider: product.bundling_with_rider,
    })

    db.commit()
    return db.query(
        product_model.Product
    ).filter(product_model.Product.id == product_id).first()


def delete_product(db: Session, product_id: int):
    db.query(
        product_model.Product
    ).filter(product_model.Product.id == product_id).delete()
    db.commit()
    return True
