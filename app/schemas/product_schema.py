from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    slug: str
    name: str
    is_active: Optional[bool] = 1
    category_id: str
    insurance_type_id: str
    featured: Optional[bool] = 0
    premium_type: str
    bundling_with_rider: Optional[bool] = 0


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: str

    class Config:
        orm_mode = True
