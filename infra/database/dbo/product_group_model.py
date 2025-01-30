from sqlalchemy import Column, Integer, String

from infra.database.dbo.base_shop_model import BaseShopModel

class ProductGroupModel(BaseShopModel):
    """"""
    product_group_id = Column(Integer, autoincrement=True, primary_key=True)
    product_group_name = Column(String, nullable=False)
    