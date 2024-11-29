from labs.lab2.functions.ConvertNumberType import ConvertNumberType

def GetOperator():
    while True:
        operator = input("Виберіть операцію ( +, -, *, /, √, %, **. ").lower()
        try:
            if operator not in ["+", "-", "*", "/", "√", "sqrt", "%", "**"]:
                raise ValueError("Недійсний оператор. Будь ласка, виберіть з +, -, *, /, √, %, **.")
            return operator
        except ValueError as e:
            print(f"Помилка: {e}")

def GetNumber():
    while True:
        num = input("Введіть число: ")
        try:
            if num == "":
                raise ValueError("Поле не може бути порожнім. Будь ласка, введіть дійсне число.")
            return ConvertNumberType(num)
        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, спробуйте ще раз.")
