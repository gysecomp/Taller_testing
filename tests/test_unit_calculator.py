#test unitario de la suma, resta y división

from src.calculator import suma, resta, division

def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 3) == 2


def test_division():
    assert division(10, 2) == 5