from sqlalchemy.orm import Session

from app.models import product_category_model as model
from app.schemas import product_category_schema as schema
from app.utils.uuid import generate_uuid


def get_product_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(
        model.ProductCategory
    ).offset(skip).limit(limit).all()


def get_product_category(db: Session, product_category_id: str):
    return db.query(
        model.ProductCategory
    ).filter(model.ProductCategory.id == product_category_id).first()


def create_user_product_category(
        db: Session,
        product_category: schema.ProductCategoryCreate):
    uuid = generate_uuid()
    db_product_category = model.ProductCategory(
        id=uuid,
        name=product_category.name,)
    db.add(db_product_category)
    db.commit()
    db.refresh(db_product_category)
    return db_product_category


def update_product_category(
            db: Session,
            product_category: schema.ProductCategoryCreate,
            product_category_id: str
        ):
    db.query(
        model.ProductCategory
    ).filter(
        model.ProductCategory.id == product_category_id
    ).update({
        model.ProductCategory.name: product_category.name,
    })

    db.commit()
    return db.query(
        model.ProductCategory
    ).filter(model.ProductCategory.id == product_category_id).first()


def delete_product_category(db: Session, product_category_id: int):
    db.query(
        model.ProductCategory
    ).filter(model.ProductCategory.id == product_category_id).delete()
    db.commit()
    return True
