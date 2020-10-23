from sqlalchemy.orm import Session
from app.repositories import product_insurance_type_repository as repository
from app.schemas import product_insurance_type_schema as schema


def get_product_insurance_types(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_product_insurance_types(db, skip=skip, limit=limit)


def get_product_insurance_type(db: Session, product_insurance_type_id: str):
    return repository.get_product_insurance_type(
        db,
        product_insurance_type_id=product_insurance_type_id)


def create_user_product_insurance_type(
        db: Session,
        product_insurance_type: schema.ProductInsuranceTypeCreate):
    return repository.create_user_product_insurance_type(
        db=db,
        product_insurance_type=product_insurance_type)


def update_product_insurance_type(
            db: Session,
            product_insurance_type: schema.ProductInsuranceTypeCreate,
            product_insurance_type_id: str
        ):
    return repository.update_product_insurance_type(
        db=db,
        product_insurance_type=product_insurance_type,
        product_insurance_type_id=product_insurance_type_id)


def delete_product_insurance_type(db: Session, product_insurance_type_id: str):
    return repository.delete_product_insurance_type(
        db=db,
        product_insurance_type_id=product_insurance_type_id)
