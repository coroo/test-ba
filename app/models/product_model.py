from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from config.database import Base


class Item(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(191), index=True)
    name = Column(String(191), index=True)
    is_active = Column(Boolean, default=True)
    category_id = Column(String(100), ForeignKey("product_categories.id"))
    insurance_type_id = Column(String(100),
                               ForeignKey("product_insurance_types.id"))
    featured = Column(Boolean, default=True)
    premium_type = Column(String(191))
    bundling_with_rider = Column(Boolean, default=True)

    category = relationship("ProductCategories", back_populates="products")
    insurance_type = relationship("ProductInsuranceTypes",
                                  back_populates="products")
