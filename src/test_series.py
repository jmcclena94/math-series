# -*- coding: utf-8 -*-
import pytest

FIB_TABLE = [
    (1, 0),
    (2, 1),
    (3, 1),
    (8, 13),
    (9, 21)
]

LUCAS_TABLE = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7)
]

SERIES_TABLE = [
    (1, 0, 1, 0),
    (1, 2, 1, 2),
    (9, 0, 1, 21),
    (3, 3, 3, 6)
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, x, y, result', SERIES_TABLE)
def test_sum_series(n, x, y, result):
    from series import sum_series
    assert sum_series(n, x, y) == result
