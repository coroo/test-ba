from sqlalchemy import Column, ForeignKey, Integer, String
from config.database import Base


class ProductPlanBenefit(Base):
    __tablename__ = "product_plan_benefits"

    id = Column(String(50), primary_key=True, index=True)
    product_plan_id = Column(String(50),
                             ForeignKey("product_plans.id"),
                             default=True)
    benefit = Column(String(191))
    value = Column(String(191))
    value_type = Column(String(191))
    order = Column(Integer, default=0)
