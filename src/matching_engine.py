from src.order import Trade
from src.order_book import OrderBook

class MatchingEngine:
    def __init__(self):
        self.book = OrderBook()
        self.trades = []
        self.trade_counter = 1

    def submit(self, order):
        self.book.add(order)
        new_trades = []

        while self.book.best_buy() and self.book.best_sell():
            buy = self.book.best_buy()
            sell = self.book.best_sell()

            # Prices must cross for a trade to happen.
            if buy.price < sell.price:
                break

            quantity = min(
                buy.remaining,
                sell.remaining
            )

            # Simplified pricing: use the earlier order's price.
            if buy.timestamp_ns <= sell.timestamp_ns:
                trade_price = buy.price
            else:
                trade_price = sell.price

            trade = Trade(
                trade_id=f"T{self.trade_counter:06d}",
                buy_order_id=buy.order_id,
                sell_order_id=sell.order_id,
                price=trade_price,
                quantity=quantity
            )

            self.trade_counter += 1
            buy.remaining -= quantity
            sell.remaining -= quantity

            self.trades.append(trade)
            new_trades.append(trade)

            self.book.remove_filled()

        return new_trades

    def snapshot(self):
        return self.book.snapshot()
    
    def submit(self, order):
        """Submit an order and match it with available opposite orders."""

        self.book.add(order)
        new_trades = []

        # Match orders while buy and sell orders are available.
        while self.book.best_buy() and self.book.best_sell():

            buy = self.book.best_buy()
            sell = self.book.best_sell()

            # Prices must cross for a trade to happen.
            if buy.price < sell.price:
                break

            # Calculate executable quantity.
            quantity = min(
                buy.remaining,
                sell.remaining
            )

            # Use the earlier order's price.
            if buy.timestamp_ns <= sell.timestamp_ns:
                trade_price = buy.price
            else:
                trade_price = sell.price

            # Create a trade record.
            trade = Trade(
                trade_id=f"T{self.trade_counter:06d}",
                buy_order_id=buy.order_id,
                sell_order_id=sell.order_id,
                price=trade_price,
                quantity=quantity
            )

            # Update order quantities.
            self.trade_counter += 1
            buy.remaining -= quantity
            sell.remaining -= quantity

            # Store executed trade.
            self.trades.append(trade)
            new_trades.append(trade)

            # Remove completed orders.
            self.book.remove_filled()

        return new_trades

    def snapshot(self):
        """Return the current order book snapshot."""
        return self.book.snapshot()
         