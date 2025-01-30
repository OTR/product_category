from sqlalchemy import Column, String
from infra.database.database import Base

class BaseShopModel(Base):
    """"""
    version = Column(String, default="master")
