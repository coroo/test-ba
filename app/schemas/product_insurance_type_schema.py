from pydantic import BaseModel


class ProductInsuranceTypeBase(BaseModel):
    name: str


class ProductInsuranceTypeCreate(ProductInsuranceTypeBase):
    pass


class ProductInsuranceType(ProductInsuranceTypeBase):
    id: str
