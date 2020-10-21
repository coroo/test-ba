from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import product_schema
from app.usecases import product_usecase
from app.middlewares import deps, di

router = APIRouter()
local_prefix = "/products/"


@router.post("/users/{user_id}"+local_prefix,
             response_model=product_schema.Product)
def create_product_for_user(
            user_id: str,
            product: product_schema.ProductCreate,
            db: Session = Depends(deps.get_db)
        ):
    return product_usecase.create_user_product(db=db,
                                               product=product,
                                               user_id=user_id)


@router.get(local_prefix, response_model=List[product_schema.Product])
def read_products(
            commons: dict = Depends(di.common_parameters),
            db: Session = Depends(deps.get_db)
        ):
    products = product_usecase.get_products(
            db,
            skip=commons['skip'],
            limit=commons['limit']
        )
    return products


@router.get(local_prefix+"{product_id}", response_model=product_schema.Product)
def read_product(product_id: str, db: Session = Depends(deps.get_db)):
    db_product = product_usecase.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return db_product
