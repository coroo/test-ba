from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import (user_schema,
                         general_schema,
                         product_detail_schema as schema)
from app.usecases.product_detail_service import ProductDetailService as usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/product_details/"


class ProductDetailController():

    @router.post(local_prefix,
                 response_model=schema.ProductDetail)
    def create_product_detail(
                product_detail: schema.ProductDetailCreate,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        return usecase.create(
            db=db,
            product_detail=product_detail)

    @router.put(local_prefix+"{product_detail_id}",
                response_model=schema.ProductDetail)
    def update_product_detail(
                product_detail_id: str,
                product_detail: schema.ProductDetailCreate,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_product_detail = usecase.read(
            db,
            product_detail_id=product_detail_id)
        if db_product_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductDetail not found")
        return usecase.update(
            db=db,
            product_detail=product_detail,
            product_detail_id=product_detail_id)

    @router.get(local_prefix, response_model=List[schema.ProductDetail])
    def read_product_details(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        product_details = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return product_details

    @router.get(local_prefix+"{product_detail_id}",
                response_model=schema.ProductDetail)
    def read_product_detail(
            product_detail_id: str,
            db: Session = Depends(deps.get_db)):
        db_product_detail = usecase.read(
            db,
            product_detail_id=product_detail_id)
        if db_product_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductDetail not found")
        return db_product_detail

    @router.delete(local_prefix, response_model=general_schema.Delete)
    def delete_product_detail(
                product_detail: schema.ProductDetailId,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_product_detail = usecase.read(
            db,
            product_detail_id=product_detail.id)
        if db_product_detail is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductDetail not found")
        usecase.delete(
            db=db,
            product_detail_id=product_detail.id)
        return {"id": product_detail.id}
