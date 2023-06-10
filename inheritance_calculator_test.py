from inheritance_calculator import InheritanceCalculator

calculator=InheritanceCalculator()

while True:
    print("Choose an operation:")
    print("(+) Addition")
    print("(-) Subtraction")
    print("(*) Multiplication")
    print("(/) Division")
    print("(**) Power")
    print("(%) Percentage")
    print("(gcf) Greatest Common Factor")
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
