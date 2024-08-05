import random

class SillyCalculator:
    def add(self, a, b):
        return f"{a} + {b} = {a + b + random.randint(1, 10)}"

    def subtract(self, a, b):
        return f"{a} - {b} = {a - b - random.randint(1, 10)}"

    def multiply(self, a, b):
        return f"{a} * {b} = {a * b * random.choice([2, 3, 4])}"

    def divide(self, a, b):
        if b == 0:
            return "Division by zero? That's a trick question!"
        return f"{a} / {b} = {a / b + random.uniform(1, 5)}"

    def respond(self, operation, a, b):
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subtract(a, b)
        elif operation == "multiply":
            return self.multiply(a, b)
        elif operation == "divide":
            return self.divide(a, b)
        else:
            return "I don't understand that operation. Try add, subtract, multiply, or divide."

# Interactive loop to use the SillyCalculator
calculator = SillyCalculator()

while True:
    command = input("Enter a command (add, subtract, multiply, divide) or 'quit' to exit: ")
    if command.lower() == "quit":
        print("Goodbye!")
        break
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(calculator.respond(command.lower(), a, b))
    except ValueError:
        print("Please enter valid numbers.")
