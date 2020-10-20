from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    owner_id: str

    class Config:
        orm_mode = True
