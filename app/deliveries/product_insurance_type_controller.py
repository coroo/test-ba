from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import (user_schema,
                         general_schema,
                         product_insurance_type_schema as schema)
from app.usecases.product_insurance_type_service import ProductInsuranceTypeService as usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/product_insurance_types/"


class ProductInsuranceTypeController():

    @router.post(local_prefix,
                 response_model=schema.ProductInsuranceType)
    def create_product_insurance_type(
                product_insurance_type: schema.ProductInsuranceTypeCreate,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        return usecase.create(
            db=db,
            product_insurance_type=product_insurance_type)

    @router.put(local_prefix+"{product_insurance_type_id}",
                response_model=schema.ProductInsuranceType)
    def update_product_insurance_type(
                product_insurance_type_id: str,
                product_insurance_type: schema.ProductInsuranceTypeCreate,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_product_insurance_type = usecase.read(
            db,
            product_insurance_type_id=product_insurance_type_id)
        if db_product_insurance_type is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductInsuranceType not found")
        return usecase.update(
            db=db,
            product_insurance_type=product_insurance_type,
            product_insurance_type_id=product_insurance_type_id)

    @router.get(local_prefix, response_model=List[schema.ProductInsuranceType])
    def read_product_insurance_types(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        product_insurance_types = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return product_insurance_types

    @router.get(local_prefix+"{product_insurance_type_id}",
                response_model=schema.ProductInsuranceType)
    def read_product_insurance_type(product_insurance_type_id: str,
                                    db: Session = Depends(deps.get_db)):
        db_product_insurance_type = usecase.read(
            db,
            product_insurance_type_id=product_insurance_type_id)
        if db_product_insurance_type is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductInsuranceType not found")
        return db_product_insurance_type

    @router.delete(local_prefix, response_model=general_schema.Delete)
    def delete_product_insurance_type(
                product_insurance_type: schema.ProductInsuranceTypeId,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_product_insurance_type = usecase.read(
            db,
            product_insurance_type_id=product_insurance_type.id)
        if db_product_insurance_type is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductInsuranceType not found")
        usecase.delete(
            db=db,
            product_insurance_type_id=product_insurance_type.id)
        return {"id": product_insurance_type.id}
