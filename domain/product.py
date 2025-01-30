from typing import Optional

from pydantic import BaseModel

class Product(BaseModel):
    """

    """
    product_id: int
    product_name: str
    base_price: int
    currency: str
