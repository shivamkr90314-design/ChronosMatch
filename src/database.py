
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


    def all_trades(self, limit=None, newest_first=False):
        """
        Retrieve trade history with optional limit and sorting.
        """

        if limit is not None:
            if not isinstance(limit, int) or isinstance(limit, bool) or limit <= 0:
                raise ValueError("Limit must be a positive integer")

        if not isinstance(newest_first, bool):
            raise ValueError("newest_first must be True or False")

        try:
            with closing(sqlite3.connect(self.db_path)) as connection:
                with connection:
                    query = """
                        SELECT trade_id, buy_order_id, sell_order_id,
                               price, quantity, timestamp
                        FROM trades
                        ORDER BY timestamp
                    """

                    if newest_first:
                        query += " DESC, trade_id DESC"
                    else:
                        query += " ASC, trade_id ASC"

                    if limit is not None:
                        query += " LIMIT ?"
                        rows = connection.execute(
                            query, (limit,)
                        ).fetchall()
                    else:
                        rows = connection.execute(query).fetchall()

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
