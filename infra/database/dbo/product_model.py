from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from infra.database.dbo.base_shop_model import BaseShopModel

class ProductModel(BaseShopModel):
    """"""
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    base_price = Column(Integer, nullable=False)
    currency = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    category = relationship('CategoryModel', backref='products')