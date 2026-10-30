import pytest

from src.order import Order
from src.matching_engine import MatchingEngine

def test_invalid_side():
    with pytest.raises(ValueError):
        Order("O1", "HOLD", 100, 1)

def test_invalid_price():
    with pytest.raises(ValueError):
        Order("O1", "BUY", 0, 1)

def test_no_match():
    engine = MatchingEngine()

    engine.submit(Order("B1", "BUY", 99, 2))
    result = engine.submit(
        Order("S1", "SELL", 100, 2)
    )

    assert result == []
    assert len(engine.trades) == 0

def test_full_match():
    engine = MatchingEngine()

    engine.submit(
        Order("B1", "BUY", 101, 5, timestamp_ns=1)
    )
    trades = engine.submit(
        Order("S1", "SELL", 100, 5, timestamp_ns=2)
    )

    assert len(trades) == 1
    assert trades[0].quantity == 5
    assert engine.snapshot()["buys"] == []
    assert engine.snapshot()["sells"] == []

def test_partial_fill():
    engine = MatchingEngine()

    engine.submit(
        Order("B1", "BUY", 101, 10, timestamp_ns=1)
    )
    trades = engine.submit(
        Order("S1", "SELL", 100, 6, timestamp_ns=2)
    )

    assert trades[0].quantity == 6
    assert engine.snapshot()["buys"][0]["remaining"] == 4

def test_price_time_priority():
    engine = MatchingEngine()

    engine.submit(
        Order("B1", "BUY", 100, 2, timestamp_ns=1)
    )
    engine.submit(
        Order("B2", "BUY", 100, 3, timestamp_ns=2)
    )

    trades = engine.submit(
        Order("S1", "SELL", 100, 2, timestamp_ns=3)
    )

    assert trades[0].buy_order_id == "B1"