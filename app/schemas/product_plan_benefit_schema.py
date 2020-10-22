from typing import Optional, List
from pydantic import BaseModel

from .product_plan_benefit_schema import ProductPlanBenefit


class ProductPlanBenefitBase(BaseModel):
    product_plan_id: str
    benefit: str
    value: Optional[str] = None
    value_type: Optional[str] = None
    order: Optional[int] = None


class ProductPlanBenefitCreate(ProductPlanBenefitBase):
    pass


class ProductPlanBenefit(ProductPlanBenefitBase):
    id: str
    benefits: Optional[List[ProductPlanBenefit]]

    class Config:
        orm_mode = True
