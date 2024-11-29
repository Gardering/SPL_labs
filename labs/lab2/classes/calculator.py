import math

class Calculator:

    def Save(self, value):
        with open('History.txt', 'a') as file:
            file.write(f"{value}\n")

    def Add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        result = a + b
        self.Save(f"{a} + {b} = {result}")
        return result

    def Subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        result = a - b
        self.Save(f"{a} - {b} = {result}")
        return result

    def Multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        result = a * b
        self.Save(f"{a} * {b} = {result}")
        return result

    def Divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.Save(f"{a} / {b} = {result}")
        return result

    def Mod(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        result = a % b if a >= 0 else (a % b + abs(b)) % abs(b)
        self.Save(f"{a} % {b} = {result}")
        return result


    def SquareRoot(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Argument must be a number")
        if number < 0:
            raise ValueError("Квадратний корінь із від’ємного числа не визначений")
        result = math.sqrt(number)
        self.Save(f"Square root of {number} = {result}")
        return result

    def Exponentiate(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        result = a ** b
        self.Save(f"{a} ** {b} = {result}")
        return result

    def GetHistory(self):
        with open("History.txt", "r") as file:
            print(file.read())

class Memory:
    def __init__(self):
        self.value = 0

    def Add(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Argument must be a number")
        self.value += number
        return self.value

    def Subtract(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Argument must be a number")
        self.value -= number
        return self.value

    def Clear(self):
        self.value = 0

    def Read(self):
        return self.value
