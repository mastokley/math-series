# coding=utf-8
import pytest


FIB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    import series
    assert series.fibonacci(n) == result


LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
    (8, 47),
    (9, 76)
]


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    import series
    assert series.lucas(n) == result


SUM_SERIES_TABLE = [
    (0, 0, 1, 0),  # fibonacci
    (1, 0, 1, 1),
    (2, 0, 1, 1),
    (3, 0, 1, 2),
    (4, 0, 1, 3),
    (5, 0, 1, 5),
    (6, 0, 1, 8),
    (7, 0, 1, 13),
    (8, 0, 1, 21),
    (9, 0, 1, 34),
    (0, 2, 1, 2),  # lucas
    (1, 2, 1, 1),
    (2, 2, 1, 3),
    (3, 2, 1, 4),
    (4, 2, 1, 7),
    (5, 2, 1, 11),
    (6, 2, 1, 18),
    (7, 2, 1, 29),
    (8, 2, 1, 47),
    (9, 2, 1, 76),
    (0, 1, 8, 1),  # something else
    (1, 1, 8, 8),
    (2, 1, 8, 9),
    (3, 1, 8, 17),
    (4, 1, 8, 26),
    (5, 1, 8, 43),
    (6, 1, 8, 69),
    (7, 1, 8, 112)
]


@pytest.mark.parametrize('n, first, second, result', SUM_SERIES_TABLE)
def test_sum_series(n, first, second, result):
    import series
    assert series.sum_series(n, first, second) == result
