# coding=utf-8


def fibonacci(n):
    """Return the nth value of the Fibonacci series for non-negative n"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth value of the lucas series for non-negative n"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """Return the nth value of a series that sums the same way as the Fibonacci
    series, but with different values for the first and second numbers in the
    series.

    By default, behaves exactly like `fibonacci()`.
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return (
            sum_series(n - 1, first, second) +
            sum_series(n - 2, first, second)
        )


if __name__ == "__main__":
    print("""
This module defines functions that implement mathematical series.

fibonacci(n):
    Returns the Fibonacci series at index `n` for non-negative n.

lucas(n):
    Returns the Lucas series at index `n` for non-negative n.

sum_series(n, first=0, second=1):
    Returns a sum series similar to the Lucas or Fibonacci series, but with
    optional user-defined base values for the indexes at 0 and 1.

>>> fibonacci(1)
1
>>> fibonacci(7)
13
>>> lucas(2)
3
>>> sum_series(1, 8, 5)
43
""")
