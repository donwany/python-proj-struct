# https://book.pythontips.com/en/latest/decorators.html

import functools
import time
import math
from functools import wraps

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("DivisionByZeroError")
            return
        return func(a, b)
    return inner


def calculate_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken in: {func.__name__}, {end-begin}")
    return inner

def currency(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'${result}'
    return wrapper

@repeat(num_times=5)
def greet(name):
    print(f"Hello, {name}")

@smart_divide
def divide(a, b):
    return a / b

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


if __name__ == '__main__':
    out = greet("World")
    print(out)
    print(divide(10, 2))

    print("="*50)
    print(factorial(5))
    print("-"*50)
    print(net_price(price=100, tax=0.05))



