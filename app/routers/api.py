from fastapi import APIRouter, Depends
from app.deliveries import items, users, products
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
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
