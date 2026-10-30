import sqlite3

class TradeDatabase:
    def __init__(self, db_path="chronosmatch.db"):
        self.db_path = db_path

        with sqlite3.connect(self.db_path) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS trades (
                    trade_id TEXT PRIMARY KEY,
                    buy_order_id TEXT NOT NULL,
                    sell_order_id TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    timestamp TEXT NOT NULL
                )
            """)

    def save_trades(self, trades):
        with sqlite3.connect(self.db_path) as connection:
            connection.executemany("""
                INSERT OR REPLACE INTO trades
                (trade_id, buy_order_id, sell_order_id,
                 price, quantity, timestamp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, [
                (
                    t.trade_id,
                    t.buy_order_id,
                    t.sell_order_id,
                    t.price,
                    t.quantity,
                    t.timestamp
                )
                for t in trades
            ])

    def all_trades(self):
        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute("""
                SELECT trade_id, buy_order_id, sell_order_id,
                       price, quantity, timestamp
                FROM trades
                ORDER BY timestamp, trade_id
            """).fetchall()

        return [
            {
                "trade_id": row[0],
                "buy_order_id": row[1],
                "sell_order_id": row[2],
                "price": row[3],
                "quantity": row[4],
                "timestamp": row[5]
            }
            for row in rows
        ]
        