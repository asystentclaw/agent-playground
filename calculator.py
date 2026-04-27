from __future__ import annotations


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('cannot divide by zero')
    return a / b


if __name__ == '__main__':
    print('add(2, 3) =', add(2, 3))
    print('subtract(10, 4) =', subtract(10, 4))
    print('multiply(6, 7) =', multiply(6, 7))
    print('divide(8, 2) =', divide(8, 2))
