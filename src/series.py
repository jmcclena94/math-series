# -*- coding: utf-8 -*-


def fibonacci(n):
    """Return n'th fibonacci value."""
    num1 = 0
    num2 = 1
    if n == 1:
        return num1
    if n == 2:
        return num2
    while n > 2:
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        n -= 1
    return num3


def lucas(n):
    """Return n'th lucas value."""
    num1 = 2
    num2 = 1
    if n == 1:
        return num1
    if n == 2:
        return num2
    while n > 2:
        num3 = num2 + num1
        num1 = num2
        num2 = num3
        n -= 1
    return num3


def sum_series(n, x=0, y=1):
        """Return n'th sum series value."""
        num1 = x
        num2 = y
        if n == 1:
            return num1
        if n == 2:
            return num2
        while n > 2:
            num3 = num2 + num1
            num1 = num2
            num2 = num3
            n -= 1
        return num3


if __name__ == "__main__":
    print("This module defines functions that implement mathematical series.")
    print(fibonacci.__name__ + "(n):")
    print(fibonacci.__doc__)
    print(lucas.__name__ + "(n):")
    print(lucas.__doc__)
    print(sum_series.__name__ + "(n, x, y):")
    print(sum_series.__doc__)
