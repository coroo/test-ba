from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from config.database import Base


class ProductInsuranceType(Base):
    __tablename__ = "product_insurance_types"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(191), unique=True, index=True)

    products = relationship("Product", back_populates="insurance_type")
