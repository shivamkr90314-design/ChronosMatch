from src.order import Order
from src.matching_engine import MatchingEngine
from src.database import TradeDatabase
from src.performance import benchmark, memoryview_demo

def main():
    engine = MatchingEngine()

    # Submit a buy order for 10 units.
    engine.submit(
        Order("BUY-001", "BUY", 101.0, 10)
    )

    # Sell 6 units. This partially fills the buy order.
    trades = engine.submit(
        Order("SELL-001", "SELL", 100.0, 6)
    )

    # Sell the remaining 4 units.
    trades += engine.submit(
        Order("SELL-002", "SELL", 101.0, 4)
    )

    database = TradeDatabase()
    database.save_trades(trades)

    print("\n===== CHRONOSMATCH =====")
    print("Trades executed:", len(trades))

    for trade in trades:
        print(
            f"{trade.trade_id} | "
            f"Buy: {trade.buy_order_id} | "
            f"Sell: {trade.sell_order_id} | "
            f"Price: {trade.price} | "
            f"Quantity: {trade.quantity}"
        )

    print("\nOrder Book:")
    print(engine.snapshot())

    print("\nSaved Trade History:")
    for trade in database.all_trades():
        print(trade)

    print("\nMemoryview Demo:")
    print(memoryview_demo())

    print("\nPerformance Benchmark:")
    print(benchmark(1000))

    print("\nProject executed successfully.")

if __name__ == "__main__":
    main()