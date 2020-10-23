from typing import Optional, List
from pydantic import BaseModel

from .product_category_schema import ProductCategory
from .product_insurance_type_schema import ProductInsuranceType
from .product_detail_schema import ProductDetail
from .product_rider_schema import ProductRider
from .product_benefit_schema import ProductBenefit
from .product_plan_schema import ProductPlan


class ProductBase(BaseModel):
    slug: str
    name: str
    is_active: Optional[bool] = 1
    featured: Optional[bool] = 0
    premium_type: str
    bundling_with_rider: Optional[bool] = 0


class ProductId(BaseModel):
    id: str


class ProductCreate(ProductBase):
    category_id: str
    insurance_type_id: str
    detail_id: str


class Product(ProductBase):
    id: str
    category: Optional[ProductCategory]
    insurance_type: Optional[ProductInsuranceType]
    detail: Optional[ProductDetail]
    riders: Optional[List[ProductRider]]
    benefits: Optional[List[ProductBenefit]]
    plans: Optional[List[ProductPlan]]

    class Config:
        orm_mode = True
