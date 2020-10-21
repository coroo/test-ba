from typing import Optional
from pydantic import BaseModel

from .product_category_schema import ProductCategory
from .product_insurance_type_schema import ProductInsuranceType
from .product_detail_schema import ProductDetail


class ProductRiderBase(BaseModel):
    slug: str
    name: str
    is_active: Optional[bool] = 1
    product_id: str
    premium_type: str


class ProductRiderCreate(ProductRiderBase):
    pass


class ProductRider(ProductRiderBase):
    id: str
    category: Optional[ProductCategory]
    insurance_type: Optional[ProductInsuranceType]
    detail: Optional[ProductDetail]

    class Config:
        orm_mode = True
