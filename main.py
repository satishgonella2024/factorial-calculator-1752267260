import math

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    return math.factorial(n)