from typing import List

from pydantic import BaseModel

from .product import Product


class ProductGroup(BaseModel):
    """
    группа других товаров содержит:
     product_group_name - имя
     product_list: List[Product] - перечень других товаров
     price_calculation_strategy: str - способ расчета цены
    """
    product_group_id: int
    product_group_name: str
    product_list: List[Product]
    price_calculation_strategy: str
