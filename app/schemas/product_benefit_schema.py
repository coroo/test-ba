from pydantic import BaseModel
from typing import Optional


class ProductBenefitBase(BaseModel):
    name: str
    benefit: Optional[str] = None
    icon: Optional[str] = None
    product_id: Optional[str] = None


class ProductBenefitCreate(ProductBenefitBase):
    pass


class ProductBenefit(ProductBenefitBase):
    id: str

    class Config:
        orm_mode = True
