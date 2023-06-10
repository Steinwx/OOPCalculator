#Paul Adrian S. Montas
#BSCOE 1-4

class Calculator:
    def __init__(self) -> None:
        pass
    def power(self, a, b):
        return a ** b
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


calculator = Calculator()

while True:
    print("Choose an operation:")
    print("(+) Addition")
    print("(-) Subtraction")
    print("(*) Multiplication")
    print("(/) Division")
    print("(**) Power")
    print("(%) Percentage")
    operation = input("=")

    num1 = float(input("Input first number: "))
    num2 = float(input("Input second number: "))

    if operation == "+":
        result = calculator.add(num1, num2)
    elif operation == "-":
        result = calculator.subtract(num1, num2)
    elif operation == "*":
        result = calculator.multiply(num1, num2)
    elif operation == "/":
        result = calculator.divide(num1, num2)
    elif operation == "%":
        result = calculator.percentage(num1, num2)
    elif operation == "**":
        result = calculator.power(num1,num2)
    else:
        print("Invalid operation")
        continue

    print("=", result)