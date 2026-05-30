from dataclasses import dataclass
from abc import ABC, abstractmethod
from decimal import Decimal
import enum


class DiscountType(enum.Enum):
    FIXE = enum.auto()
    PERSONAL = enum.auto()
    LOYALTY = enum.auto()


@dataclass
class Order:
    total: Decimal
    is_loyal: bool
    is_discountable: bool


class BaseDiscount(ABC):
    @abstractmethod
    def apply(self, order: Order) -> Decimal:
        ...


class FixeDiscount(BaseDiscount):
    def apply(self, order: Order) -> Decimal:
        ...


class PercentDiscount(BaseDiscount):
    def apply(self, order: Order) -> Decimal:
        ...


class LoyaltyDiscount(BaseDiscount):
    def apply(self, order: Order) -> Decimal:
        ...


class DiscountService:
    _discount: dict[DiscountType, BaseDiscount] = {
        DiscountType.FIXE: FixeDiscount(),
        DiscountType.PERSONAL: PercentDiscount(),
        DiscountType.LOYALTY: LoyaltyDiscount(),
    }

    def get_discount(self, order: Order) -> list[BaseDiscount]:
        discounts = []
        if order.is_loyal:
            discounts.append(self._discount[DiscountType.LOYALTY])
        if order.is_discountable:
            discounts.append(self._discount[DiscountType.FIXE])
        return discounts

    def apply_discounts(self, order: Order) -> Decimal:
        discounts = self.get_discount(order)
        for discount in discounts:
            discount.apply(order)
            ...
