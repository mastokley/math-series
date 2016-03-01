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


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fib(n, result):
    import series
    assert series.fibonacci(n) == result
