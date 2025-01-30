from typing import List

from pydantic import BaseModel

from .product import Product


class ProductGroup(BaseModel):
    """

    """
    product_group_name: str
    product_list: List[Product]
    price_calculation_strategy: str
