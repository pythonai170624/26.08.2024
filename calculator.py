
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
        raise ValueError("factorial() not defined for negative values")
    return a / b

def power(a: int, b: int) -> int:
    return a ** b

def sqrt(a: int) -> float:
    return math.sqrt(a)

def is_prime(a: int) -> bool:
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, (a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True

def factorial(a: int) -> int:
    # 0:0 -> 1
    # 1:1 -> 1
    # 2:1*2  0 1 / 1 0
    # 3:1*2*3  1 2 3 / 1 3 2 / 2 1 3 / 2 3 1 / 3 1 2 / 3 2 1
    # 5:1*2*3*4*5
    if a < 0:
        raise ValueError("factorial not defined for negative values")
    result: int = 1
    if a <= 2:
        return 1
    for mul in range(2, a + 1):  # 2 3 4 5
        result = result * mul
    return result



# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working

if __name__ == "__main__":  # False when running main.py and importing
    print('**************')
    divide(3, 0)
    x: int = int(input("number:"))
    y: int = int(input("number:"))
