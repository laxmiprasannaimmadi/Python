class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError:
            raise TypeError("Input is not a number")

    def subtract(self, a, b):
        try:
            return a - b
        except TypeError:
            raise TypeError("Input is not a number")

    def multiply(self, a, b):
        try:
            return a * b
        except TypeError:
            raise TypeError("Input is not a number")

    def division(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Division by zero is not possible.")
            return a / b
        except TypeError:
            raise TypeError("Input is not a number")
        

class CalculatorUser:
    def __init__(self):
        self.calculator = Calculator()

    def use_calculator(self):
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            method = input("Choose below to operate on the above numbers: add. addition\n sub.subtract\n multiply.multiply\n div.division\n")
            
            match method:
                case "add":
                    print(f"addition of {a} + {b} = {self.calculator.add(a, b)}")
                case "sub":
                    print(f"subtraction of {a} - {b} = {self.calculator.subtract(a, b)}")
                case "multiply":
                    print(f"multiplication of {a} * {b} = {self.calculator.multiply(a, b)}")
                case "div":
                    print(f"division of {a} / {b} = {self.calculator.division(a, b)}")
                case _:
                    print("Choose the correct calculator method")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError as e:
            print(e)
        except TypeError as e:
            print(e)

if __name__ == "__main__":
    user = CalculatorUser()
    user.use_calculator()