from dataclasses import dataclass


@dataclass(repr=True, order=True, frozen=False)
class Inventory:
    name: str
    unit_price: float
    quantity_at_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_at_hand