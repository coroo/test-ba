from fastapi import APIRouter, Depends
from app.deliveries import (
        item_controller,
        user_controller,
        product_controller,
        product_category_controller,
        product_detail_controller,
        product_insurance_type_controller,
    )
from app.middlewares import auth

api = APIRouter()


api.include_router(
    user_controller.router,
    tags=["users"])
api.include_router(
    item_controller.router,
    tags=["items"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_controller.router,
    tags=["products"],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_category_controller.router,
    tags=["product_categories"],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_detail_controller.router,
    tags=["product_details"],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    product_insurance_type_controller.router,
    tags=["product_insurance_types"],
    responses={404: {"description": "Not found"}},
)
