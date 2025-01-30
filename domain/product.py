from pydantic import BaseModel

class Product(BaseModel):
    """
    Обычный товар содержит:
     product_name: str - имя
     base_price: int - цену
     currency: str - валюту

    category_id: int - Все товары онлайн магазина должны быть распределены по категориям.
    """
    product_id: int
    product_name: str
    base_price: int
    currency: str
    category_id: int
