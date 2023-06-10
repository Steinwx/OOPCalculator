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
        if b != 0:
            return a / b
        else:
            return "Math ERROR"
    def percentage(self, a, b):
        return (a * b) / 100