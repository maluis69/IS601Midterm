import pytest
from calculator.core import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(1, 0)
