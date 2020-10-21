from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from config.database import Base

from .product_category_model import ProductCategory
from .product_insurance_type_model import ProductInsuranceType
from .product_detail_model import ProductDetail


class ProductRider(Base):
    __tablename__ = "product_riders"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(191), index=True)
    name = Column(String(191), index=True)
    is_active = Column(Boolean, default=True)
    category_id = Column(String(50),
                         ForeignKey("product_categories.id"),
                         nullable=True)
    insurance_type_id = Column(String(100),
                               ForeignKey("product_insurance_types.id"),
                               nullable=True)
    detail_id = Column(String(50),
                       ForeignKey("product_details.id"),
                       nullable=True)
    product_id = Column(String(50),
                        ForeignKey("products.id"),
                        default=True)
    premium_type = Column(String(191))

    category = relationship(ProductCategory, back_populates="riders")
    insurance_type = relationship(ProductInsuranceType,
                                  back_populates="riders")
    detail = relationship(ProductDetail, back_populates="riders")
