from sqlalchemy import Column, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from config.database import Base

from .product_category_model import ProductCategory
from .product_insurance_type_model import ProductInsuranceType
from .product_detail_model import ProductDetail
from .product_rider_model import ProductRider
from .product_benefit_model import ProductBenefit
from .product_plan_model import ProductPlan


class Product(Base):
    __tablename__ = "products"

    id = Column(String(50), primary_key=True, index=True)
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
    featured = Column(Boolean, default=True)
    premium_type = Column(String(191))
    bundling_with_rider = Column(Boolean, default=True)

    category = relationship(ProductCategory, back_populates="products")
    insurance_type = relationship(ProductInsuranceType,
                                  back_populates="products")
    detail = relationship(ProductDetail, back_populates="products")
    riders = relationship(ProductRider, backref="product", lazy="select")
    benefits = relationship(ProductBenefit, backref="product", lazy="select")
    plans = relationship(ProductPlan, backref="product", lazy="select")
