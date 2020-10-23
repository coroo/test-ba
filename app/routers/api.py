from fastapi import APIRouter, Depends
from app.deliveries import (items,
                            users,
                            products,
                            product_categories,
                            product_details,
                            product_insurance_types,)
from app.middlewares import auth

api = APIRouter()


api.include_router(
    users.router,
    tags=["users"])
api.include_router(
    items.router,
    tags=["items"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    products.router,
    tags=["products"],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_categories.router,
    tags=["product_categories"],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_details.router,
    tags=["product_details"],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_insurance_types.router,
    tags=["product_insurance_types"],
    responses={404: {"description": "Not found"}},
)
