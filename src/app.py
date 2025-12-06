import math

# Basic Operations
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Advanced Operations
def log(x):
    """Calculate natural logarithm of x. Raises ValueError if x <= 0."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(x)

def square(x):
    """Calculate square of x."""
    return x ** 2

def sin(x):
    """Calculate sine of x (x in radians)."""
    return math.sin(x)

def cos(x):
    """Calculate cosine of x (x in radians)."""
    return math.cos(x)

def sqrt(x):
    """Calculate square root of x. Raises ValueError if x < 0."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def percentage(x, y):
    """Calculate x percent of y."""
    return (x / 100) * y