import sys
from pathlib import Path
import pytest
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, subtract, multiply, divide, log, square, sin, cos, sqrt, percentage


# ========== BASIC OPERATIONS TESTS ==========

# Addition Tests
def test_add_positive():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-5, -6) == -11

def test_add_mixed():
    assert add(5, -3) == 2

def test_add_zero():
    assert add(0, 5) == 5

def test_add_decimals():
    assert add(2.5, 3.5) == 6.0


# Subtraction Tests
def test_subtract_positive():
    assert subtract(10, 6) == 4

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_mixed():
    assert subtract(5, 8) == -3

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_decimals():
    assert subtract(10.5, 2.5) == 8.0


# Multiplication Tests
def test_multiply_positive():
    assert multiply(5, 6) == 30

def test_multiply_negative():
    assert multiply(-5, -6) == 30

def test_multiply_mixed():
    assert multiply(-5, 6) == -30

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_multiply_decimals():
    assert multiply(2.5, 4) == 10.0


# Division Tests
def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, -2) == 5

def test_divide_mixed():
    assert divide(-10, 2) == -5

def test_divide_decimals():
    assert divide(7.5, 2.5) == 3.0

def test_divide_by_zero():
    """Test that division by zero raises ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_zero_numerator():
    assert divide(0, 5) == 0


# ========== ADVANCED OPERATIONS TESTS ==========

# Logarithm Tests
def test_log_positive():
    assert log(math.e) == pytest.approx(1.0)

def test_log_one():
    assert log(1) == 0

def test_log_large_number():
    assert log(100) == pytest.approx(4.605170, rel=1e-5)

def test_log_zero():
    """Test that log(0) raises ValueError"""
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        log(0)

def test_log_negative():
    """Test that log of negative number raises ValueError"""
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        log(-5)


# Square Tests
def test_square_positive():
    assert square(5) == 25

def test_square_negative():
    assert square(-5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_decimal():
    assert square(2.5) == 6.25


# Sine Tests
def test_sin_zero():
    assert sin(0) == pytest.approx(0.0)

def test_sin_pi_over_2():
    assert sin(math.pi / 2) == pytest.approx(1.0)

def test_sin_pi():
    assert sin(math.pi) == pytest.approx(0.0, abs=1e-10)

def test_sin_negative():
    assert sin(-math.pi / 2) == pytest.approx(-1.0)


# Cosine Tests
def test_cos_zero():
    assert cos(0) == pytest.approx(1.0)

def test_cos_pi_over_2():
    assert cos(math.pi / 2) == pytest.approx(0.0, abs=1e-10)

def test_cos_pi():
    assert cos(math.pi) == pytest.approx(-1.0)

def test_cos_negative():
    assert cos(-math.pi) == pytest.approx(-1.0)


# Square Root Tests
def test_sqrt_positive():
    assert sqrt(25) == 5.0

def test_sqrt_zero():
    assert sqrt(0) == 0.0

def test_sqrt_decimal():
    assert sqrt(2.25) == 1.5

def test_sqrt_large_number():
    assert sqrt(144) == 12.0

def test_sqrt_negative():
    """Test that sqrt of negative number raises ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        sqrt(-5)


# Percentage Tests
def test_percentage_basic():
    assert percentage(10, 100) == 10.0

def test_percentage_fifty():
    assert percentage(50, 200) == 100.0

def test_percentage_decimal():
    assert percentage(25.5, 80) == 20.4

def test_percentage_zero():
    assert percentage(0, 100) == 0.0

def test_percentage_of_zero():
    assert percentage(50, 0) == 0.0

def test_percentage_over_hundred():
    assert percentage(150, 50) == 75.0