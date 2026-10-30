from src.order import Order

class OrderBook:
    def __init__(self):
        self.buys = []
        self.sells = []
        self.order_ids = set()

    def add(self, order: Order):
        if order.order_id in self.order_ids:
            raise ValueError(
                f"Duplicate order ID: {order.order_id}"
            )

        self.order_ids.add(order.order_id)

        if order.side == "BUY":
            self.buys.append(order)
            self.buys.sort(
                key=lambda o: (
                    -o.price,
                    o.timestamp_ns,
                    o.order_id
                )
            )
        else:
            self.sells.append(order)
            self.sells.sort(
                key=lambda o: (
                    o.price,
                    o.timestamp_ns,
                    o.order_id
                )
            )

    def best_buy(self):
        return self.buys[0] if self.buys else None

    def best_sell(self):
        return self.sells[0] if self.sells else None

    def remove_filled(self):
        self.buys = [
            order for order in self.buys
            if order.remaining > 0
        ]
        self.sells = [
            order for order in self.sells
            if order.remaining > 0
        ]

    def snapshot(self):
        return {
            "buys": [
                {
                    "order_id": o.order_id,
                    "price": o.price,
                    "remaining": o.remaining
                }
                for o in self.buys
            ],
            "sells": [
                {
                    "order_id": o.order_id,
                    "price": o.price,
                    "remaining": o.remaining
                }
                for o in self.sells
            ]
        }