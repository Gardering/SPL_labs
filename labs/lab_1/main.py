import math


def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                raise ValueError("Введення порожнього поля недопустиме.")
            return float(value)
        except ValueError as e:
            print(f"Помилка: {e}")


def get_operation():
    operations = {
        "+": "додавання",
        "-": "віднімання",
        "*": "множення",
        "/": "ділення",
        "^": "піднесення до степеня",
        "sqrt": "корінь квадратний",
        "%": "процент"
    }
    print("\nОберіть операцію:")
    for op, desc in operations.items():
        print(f"'{op}' - {desc}")

    while True:
        op = input("Операція: ").strip()
        if op in operations:
            return op
        print("Невідома операція. Спробуйте ще раз.")


def calculate():
    print("=== Консольний калькулятор ===")

    while True:
        operation = get_operation()

        if operation == "sqrt":
            num = get_number("Введіть число: ")
            if num < 0:
                print("Помилка: не можна взяти корінь із від’ємного числа.")
            else:
                print(f"Результат: √{num} = {math.sqrt(num)}")
        else:
            num1 = get_number("Введіть перше число: ")
            num2 = get_number("Введіть друге число: ")

            if operation == "+":
                print(f"Результат: {num1} + {num2} = {num1 + num2}")
            elif operation == "-":
                print(f"Результат: {num1} - {num2} = {num1 - num2}")
            elif operation == "*":
                print(f"Результат: {num1} * {num2} = {num1 * num2}")
            elif operation == "/":
                if num2 == 0:
                    print("Помилка: ділення на нуль недопустиме.")
                else:
                    print(f"Результат: {num1} / {num2} = {num1 / num2}")
            elif operation == "^":
                print(f"Результат: {num1} ^ {num2} = {math.pow(num1, num2)}")
            elif operation == "%":
                print(f"Результат: {num1} % {num2} = {(num1 * num2) / 100}")

        again = input("\nВиконати ще одну операцію? (так/ні): ").strip().lower()
        if again != "так":
            print("Дякую за використання калькулятора. До побачення!")
            break


if __name__ == "__main__":
    calculate()
