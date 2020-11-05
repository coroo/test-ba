from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import product_insurance_type_model as model
from app.schemas import product_insurance_type_schema as schema
from app.utils.uuid import generate_uuid


class ProductInsuranceTypeRepository(RepositoryInterface):

    def get_product_insurance_types(
            db: Session,
            skip: int = 0,
            limit: int = 100):
        return db.query(
            model.ProductInsuranceType
        ).offset(skip).limit(limit).all()

    def get_product_insurance_type(
            db: Session,
            product_insurance_type_id: str):
        return db.query(
            model.ProductInsuranceType
        ).filter(
            model.ProductInsuranceType.id == product_insurance_type_id
        ).first()

    def create_user_product_insurance_type(
            db: Session,
            product_insurance_type: schema.ProductInsuranceTypeCreate):
        uuid = generate_uuid()
        db_product_insurance_type = model.ProductInsuranceType(
            id=uuid,
            name=product_insurance_type.name,)
        db.add(db_product_insurance_type)
        db.commit()
        db.refresh(db_product_insurance_type)
        return db_product_insurance_type

    def update_product_insurance_type(
                db: Session,
                product_insurance_type: schema.ProductInsuranceTypeCreate,
                product_insurance_type_id: str
            ):
        db.query(
            model.ProductInsuranceType
        ).filter(
            model.ProductInsuranceType.id == product_insurance_type_id
        ).update({
            model.ProductInsuranceType.name: product_insurance_type.name,
        })

        db.commit()
        return db.query(
            model.ProductInsuranceType
        ).filter(
            model.ProductInsuranceType.id == product_insurance_type_id
        ).first()

    def delete_product_insurance_type(
            db: Session,
            product_insurance_type_id: int):
        db.query(
            model.ProductInsuranceType
        ).filter(
            model.ProductInsuranceType.id == product_insurance_type_id
        ).delete()
        db.commit()
        return True
