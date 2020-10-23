from pydantic import BaseModel


class ProductInsuranceTypeBase(BaseModel):
    name: str


class ProductInsuranceTypeId(BaseModel):
    id: str


class ProductInsuranceTypeCreate(ProductInsuranceTypeBase):
    pass


class ProductInsuranceType(ProductInsuranceTypeBase):
    id: str

    class Config:
        orm_mode = True
