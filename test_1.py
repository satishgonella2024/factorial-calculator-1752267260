import pytest

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test Cases
def test_positive_input():
    assert factorial(5) == 120

def test_zero_input():
    assert factorial(0) == 1

def test_negative_input():
    with pytest.raises(ValueError):
        factorial(-5)

def test_non_integer_input():
    with pytest.raises(ValueError):
        factorial(5.5)