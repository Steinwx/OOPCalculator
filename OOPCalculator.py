#Paul Adrian S. Montas
#BSCOE 1-4

class Calculator:
    def __init__(self) -> None:
        pass
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b

calculator = Calculator()

print(calculator.add(10,10))
print(calculator.subtract(10,10))
print(calculator.divide(10,10))
print(calculator.multiply(10,10))
print(calculator.add(0,0))
print(calculator.multiply(20,20))