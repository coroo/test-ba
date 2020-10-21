from sqlalchemy import Column, ForeignKey, Integer, String
from config.database import Base


class ProductPlan(Base):
    __tablename__ = "product_plans"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(191))
    product_id = Column(String(50),
                        ForeignKey("products.id"),
                        default=True)
    product_code = Column(String(191), index=True)
    product_plan_code = Column(String(191), index=True)
    icon = Column(String(191), nullable=True)
    sum_assured = Column(Integer, default=0)
    discount = Column(Integer, default=0)
    type = Column(String(191), nullable=True)
    monthly_premium = Column(Integer, default=0)
    yearly_premium = Column(Integer, default=0)
