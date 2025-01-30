from typing import List

from application.use_case.base_price_calc_strategy import BasePriceCalcStrategy
from domain.product import Product


class CalculatePriceUseCase:

    def __init__(self, calc_strategy: BasePriceCalcStrategy):
        self.calc_strategy: BasePriceCalcStrategy = calc_strategy

    def execute(self, product_list: List[Product]) -> int:
        return self.calc_strategy.execute(product_list)
