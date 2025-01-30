from abc import ABC, abstractmethod
from typing import List

from domain.product import Product


class BasePriceCalcStrategy(ABC):

    @abstractmethod
    def execute(self, product_list: List[Product]) -> int:
        """"""
