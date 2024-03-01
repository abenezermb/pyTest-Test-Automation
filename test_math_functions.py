# test_math_functions.py

import pytest
from math_functions import add, subtract, multiply, divide

# Test cases for addition function
def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Test cases for subtraction function
def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(10, -3) == 13
    assert subtract(0, 0) == 0

# Test cases for multiplication function
def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-1, 4) == -4
    assert multiply(0, 5) == 0

# Test cases for division function
def test_division():
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
