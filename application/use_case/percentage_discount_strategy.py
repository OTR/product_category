from typing import List

from application.use_case.base_price_calc_strategy import BasePriceCalcStrategy
from domain.product import Product


class PercentageDiscountStrategy(BasePriceCalcStrategy):

    def __init__(self, discount_rate: float):
        super().__init__()
        self.discount_rate: float = discount_rate

    def execute(self, product_list: List[Product]) -> int:
        """"""
        total_price = sum(product.base_price for product in product_list)

        return int(total_price * (1 - self.discount_rate))

BackoffStrategy = PercentageDiscountStrategy(0.0)
TenPercentDiscountStrategy = PercentageDiscountStrategy(0.1)
FifteenPercentDiscountStrategy = PercentageDiscountStrategy(0.15)
