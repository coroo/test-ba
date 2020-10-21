from pydantic import BaseModel
from typing import Optional


class ProductDetailBase(BaseModel):
    summary: str
    description: Optional[str] = None
    icon: Optional[str] = None
    coverage_period: Optional[str] = None


class ProductDetailCreate(ProductDetailBase):
    pass


class ProductDetail(ProductDetailBase):
    id: str

    class Config:
        orm_mode = True
