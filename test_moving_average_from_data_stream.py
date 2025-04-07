from math import isclose
from moving_average_from_data_stream import MovingAverage


def test_ex1():
    size = 3
    moving_average = MovingAverage(size)
    result = moving_average.next(1)
    assert isclose(result, 1.0, rel_tol=1e-16)
    result = moving_average.next(10)
    assert isclose(result, 5.5, rel_tol=1e-16)
    result = moving_average.next(3)
    assert isclose(result, 4.66667, rel_tol=1e-6)
    result = moving_average.next(5)
    assert isclose(result, 6.0, rel_tol=1e-16)
