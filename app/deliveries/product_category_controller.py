from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import (user_schema,
                         general_schema,
                         product_category_schema as schema)
from app.usecases.product_category_service import (
    ProductCategoryService as usecase)
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/product_categories/"


class ProductCategoryController():

    @router.post(local_prefix,
                 response_model=schema.ProductCategory)
    def create_product_category(
                product_category: schema.ProductCategoryCreate,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        return usecase.create(
            db=db,
            product_category=product_category)

    @router.put(local_prefix+"{product_category_id}",
                response_model=schema.ProductCategory)
    def update_product_category(
                product_category_id: str,
                product_category: schema.ProductCategoryCreate,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_product_category = usecase.read(
            db,
            product_category_id=product_category_id)
        if db_product_category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product Category not found")
        return usecase.update(
            db=db,
            product_category=product_category,
            product_category_id=product_category_id)

    @router.get(local_prefix,
                response_model=List[schema.ProductCategory])
    def read_product_categories(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        product_categories = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return product_categories

    @router.get(local_prefix+"{product_category_id}",
                response_model=schema.ProductCategory)
    def read_product_category(product_category_id: str,
                              db: Session = Depends(deps.get_db)):
        db_product_category = usecase.read(
            db,
            product_category_id=product_category_id)
        if db_product_category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductCategory not found")
        return db_product_category

    @router.delete(local_prefix, response_model=general_schema.Delete)
    def delete_product_category(
                product_category: schema.ProductCategoryId,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_product_category = usecase.read(
            db,
            product_category_id=product_category.id)
        if db_product_category is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="ProductCategory not found")
        usecase.delete(
            db=db,
            product_category_id=product_category.id)
        return {"id": product_category.id}
