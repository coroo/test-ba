from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from config.database import Base


class ProductBenefit(Base):
    __tablename__ = "product_benefits"

    id = Column(String(50), primary_key=True, index=True)
    product_id = Column(String(50),
                        ForeignKey("products.id"),
                        default=True)
    name = Column(String(191))
    benefit = Column(String(255))
    icon = Column(String(255))

    products = relationship("Product", back_populates="benefits")
