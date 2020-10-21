from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from config.database import Base


class ProductDetail(Base):
    __tablename__ = "product_details"

    id = Column(String(50), primary_key=True, index=True)
    summary = Column(String(191))
    description = Column(String(255))
    icon = Column(String(255))
    coverage_period = Column(String(191))

    products = relationship("Product", back_populates="detail")
    riders = relationship("ProductRider",
                          back_populates="detail")
