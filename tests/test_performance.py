from src.performance import benchmark, memoryview_demo


def test_benchmark_result():
    result = benchmark(100)

    assert result["orders"] == 100
    assert result["elapsed_seconds"] >= 0
    assert result["orders_per_second"] > 0


def test_memoryview_demo():
    result = memoryview_demo()

    assert result["original_buffer"] == "CHRONOSMATCH"
    assert result["view_sample"] == "CHRONO"
    assert "explanation" in result
    