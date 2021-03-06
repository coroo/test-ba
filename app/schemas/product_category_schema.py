from pydantic import BaseModel


class ProductCategoryBase(BaseModel):
    name: str


class ProductCategoryId(BaseModel):
    id: str


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategory(ProductCategoryBase):
    id: str

    class Config:
        orm_mode = True
