from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.product_insurance_type_repository import (
    ProductInsuranceTypeRepository as repository)
from app.schemas import product_insurance_type_schema as schema


class ProductInsuranceTypeService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return repository.reads(db, skip=skip, limit=limit)

    def read(db: Session, product_insurance_type_id: str):
        return repository.read(
            db,
            product_insurance_type_id=product_insurance_type_id)

    def create(
            db: Session,
            product_insurance_type: schema.ProductInsuranceTypeCreate):
        return repository.create(
            db=db,
            product_insurance_type=product_insurance_type)

    def update(
                db: Session,
                product_insurance_type: schema.ProductInsuranceTypeCreate,
                product_insurance_type_id: str
            ):
        return repository.update(
            db=db,
            product_insurance_type=product_insurance_type,
            product_insurance_type_id=product_insurance_type_id)

    def delete(db: Session, product_insurance_type_id: str):
        return repository.delete(
            db=db,
            product_insurance_type_id=product_insurance_type_id)
