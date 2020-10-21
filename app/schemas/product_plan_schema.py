from typing import Optional
from pydantic import BaseModel


class ProductPlanBase(BaseModel):
    name: str
    product_id: str
    product_code: str
    product_plan_code: str
    icon: str
    sum_assured: int
    discount: Optional[int] = 0
    type: str
    monthly_premium: int
    yearly_premium: int


class ProductPlanCreate(ProductPlanBase):
    pass


class ProductPlan(ProductPlanBase):
    id: str

    class Config:
        orm_mode = True
