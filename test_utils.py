import pytest
import utils

@pytest.mark.parametrize("a, b, expected", [(1 , 2 , 3) , (2 , 3 ,5) , (3 , 4 , 7) , (4 , 5 , 9)])

def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(2 , 1 , 1) , (8 , 3 ,5) , (11 , 4 , 7) , (14 , 5 , 9)])

def test_substract(a, b, expected):
    result = utils.substract(a,b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(1 , 2 , 2) , (2 , 3 ,6) , (3 , 4 , 12) , (4 , 5 , 20)])

def test_multiply(a, b, expected):
    result = utils.multiply(a,b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(6 , 2 , 3) , (15 , 3 ,5) , (28 , 4 , 7) , (5 , 2 , 2.5)])

def test_divide(a, b, expected):
    result = utils.substract(a,b)
    assert result == expected

@pytest.mark.parametrize("a, expected", [(6 , 36) , (15 ,225) , (4 , 16) , (5 , 25)])

def test_square(a, expected):
    result = utils.square(a)
    assert result == expected


