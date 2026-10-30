import time
from src.order import Order
from src.matching_engine import MatchingEngine

def memoryview_demo():
    data = bytearray(b"CHRONOSMATCH")
    view = memoryview(data)

    return {
        "original_buffer": data.decode("ascii"),
        "view_sample": view[:6].tobytes().decode("ascii"),
        "explanation": (
            "memoryview provides a view of the existing buffer. "
            "Calling tobytes() creates a copy."
        )
    }

def benchmark(order_count=1000):
    engine = MatchingEngine()

    start = time.perf_counter()

    for i in range(order_count):
        if i % 2 == 0:
            side = "BUY"
            price = 99.0
        else:
            side = "SELL"
            price = 101.0

        engine.submit(
            Order(
                order_id=f"ORD-{i:06d}",
                side=side,
                price=price,
                quantity=1
            )
        )

    elapsed = time.perf_counter() - start

    return {
        "orders": order_count,
        "elapsed_seconds": round(elapsed, 6),
        "orders_per_second": round(
            order_count / elapsed, 2
        ) if elapsed else None
    }