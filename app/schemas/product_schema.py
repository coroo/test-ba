from typing import Optional
from pydantic import BaseModel

from .product_category_schema import ProductCategory
from .product_insurance_type_schema import ProductInsuranceType


class ProductBase(BaseModel):
    slug: str
    name: str
    is_active: Optional[bool] = 1
    featured: Optional[bool] = 0
    premium_type: str
    bundling_with_rider: Optional[bool] = 0


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: str
    category: ProductCategory
    insurance_type: ProductInsuranceType

    class Config:
        orm_mode = True
