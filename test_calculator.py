# from Terminal > pip install pytest
# from Terminal > pytest .
import pytest
import math

import calculator

def test_calculator_add_small():
    # Arrange
    x: int = -1
    y: int = 0
    expected: int = -1

    # Act
    actual: int = calculator.add(x, y)

    # list1 = []
    # list1.append(1)
    # assert list1[len(list1) - 1] == 1

    # Assert
    assert actual == expected

def test_calculator_sub_small():
    # Arrange
    x: int = 14
    y: int = 7
    expected: int = 7

    # Act
    actual: int = calculator.subtract(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_small():
    # Arrange
    x: int = 8
    y: int = 9
    expected: int = 72

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_mul_zero():
    # Arrange
    x: int = 1000
    y: int = 0
    expected: int = 0

    # Act
    actual: int = calculator.multiply(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_small():
    # Arrange
    x: int = 99
    y: int = 11
    expected: int = 9

    # Act
    actual: int = calculator.divide(x, y)

    # Assert
    assert actual == expected

def test_calculator_div_zero_error_phase1():
    # test that we get an error when divide by zero
    # Arrange
    x: int = 99
    y: int = 0

    # Act
    try:
        actual: int = calculator.divide(x, y)
        assert False  # fail the test
    except ZeroDivisionError as e:
        assert True  # pass the test

def test_calculator_div_zero_error_phase2():
    x: int = 99
    y: int = 0
    with pytest.raises(ZeroDivisionError) as ex:
        actual: int = calculator.divide(x, y)

    assert str(ex.value) == "Cannot divide by zero!"

def test_calculator_power_2_4_16():
    # Arrange
    x: int = 2
    y: int = 4
    expected: int = 2 ** 4

    # Act
    actual: int = calculator.power(x, y)

    # Assert
    assert actual == expected


def test_calculator_power_3_2_9():
    # Arrange
    x: int = 3
    y: int = 2
    expected: int = 3 ** 2

    # Act
    actual: int = calculator.power(x, y)

    # Assert
    assert actual == expected


def test_calculator_power_9_0_1():
    # Arrange
    x: int = 9
    y: int = 0
    expected: int = 9 ** 0

    # Act
    actual: int = calculator.power(x, y)

    # Assert
    assert actual == expected


def test_calculator_sqrt_25():
    # Arrange
    x: int = 25
    expected: int = math.sqrt(x)

    # Act
    actual: int = calculator.sqrt(x)

    # Assert
    assert actual == expected

def test_calculator_sqrt_minus_5():
    # Arrange
    x: int = -5
    math.sqrt(25)
    # check if this scenario we get an error
    # if we don't get --> test should fail
    # if we get error -> test should pass
    with pytest.raises(ValueError) as ex:
        calculator.sqrt(-25)

    assert str(ex.value) == "math domain error"


