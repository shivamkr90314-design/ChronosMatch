
from dataclasses import dataclass
from datetime import datetime, timezone
import time

@dataclass
class Order:
    order_id: str
    side: str
    price: float
    quantity: int
    timestamp_ns: int = 0
    remaining: int = 0

    def __post_init__(self):
        self.side = self.side.upper()

        if self.side not in ("BUY", "SELL"):
            raise ValueError("Side must be BUY or SELL")

        if not self.order_id.strip():
            raise ValueError("Order ID cannot be empty")

        if self.price <= 0:
            raise ValueError("Price must be positive")

        if isinstance(self.quantity, bool) or not isinstance(
            self.quantity, int
        ) or self.quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        self.timestamp_ns = self.timestamp_ns or time.time_ns()

        if self.remaining == 0:
            self.remaining = self.quantity

        if not 0 <= self.remaining <= self.quantity:
            raise ValueError("Invalid remaining quantity")

@dataclass
class Trade:
    trade_id: str
    buy_order_id: str
    sell_order_id: str
    price: float
    quantity: int
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(
                timezone.utc
            ).isoformat()