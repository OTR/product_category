from sqlalchemy import Column, String, Integer, ForeignKey

from infra.database.dbo.base_shop_model import BaseShopModel

class CategoryModel(BaseShopModel):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('category.category_id'), nullable=True)
    