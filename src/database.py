
import sqlite3
from contextlib import closing

class TradeDatabase:

    def __init__(self, db_path="chronosmatch.db"):
        self.db_path = db_path

        try:
            with closing(sqlite3.connect(self.db_path)) as connection:
                with connection:
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

        except sqlite3.Error as error:
            raise RuntimeError(
                f"Database initialization failed: {error}"
            ) from error

    def save_trades(self, trades):

        try:
            with closing(sqlite3.connect(self.db_path)) as connection:
                with connection:
                    connection.executemany("""
                        INSERT OR REPLACE INTO trades
                        (
                            trade_id,
                            buy_order_id,
                            sell_order_id,
                            price,
                            quantity,
                            timestamp
                        )
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

        except sqlite3.Error as error:
            raise RuntimeError(
                f"Failed to save trades: {error}"
            ) from error

    def all_trades(self):

        try:
            with closing(sqlite3.connect(self.db_path)) as connection:
                with connection:
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

        except sqlite3.Error as error:
            raise RuntimeError(
                f"Failed to retrieve trades: {error}"
            ) from error