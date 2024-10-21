import pytest
from example import add, subtract, multiply, divide

def test_add():
    """Test the add function."""
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(-6, 2) == -3

    # Test division by zero raises an error
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
