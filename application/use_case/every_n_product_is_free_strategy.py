from typing import List, Iterable

from application.use_case.base_price_calc_strategy import BasePriceCalcStrategy
from domain.product import Product


class EveryNProductIsFreeStrategy(BasePriceCalcStrategy):

    def __init__(self, every_n: int):
        # TODO: validate that `every_n` is greater than 1
        super().__init__()
        self.every_n: int = every_n

    def execute(self, product_list: List[Product]) -> int:
        """"""
        sorted_prices: Iterable[int] = sorted((product.base_price for product in product_list))
        total_price: int = sum(sorted_prices)
        product_amount: int = len(product_list)

        if product_amount < self.every_n:
            return total_price

        products_for_free: int = product_amount // self.every_n

        return sum(sorted_prices[products_for_free:])

EveryFifthProductIsFreeStrategy = EveryNProductIsFreeStrategy(5)
