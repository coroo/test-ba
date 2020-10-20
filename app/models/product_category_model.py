from sqlalchemy import Column, String

from config.database import Base


class User(Base):
    __tablename__ = "product_categories"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(191), unique=True, index=True)
