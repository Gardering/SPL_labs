from classes.calculator import Calculator, Memory
from functions.ErrorHandler import GetOperator, GetNumber


def main():
    calc = Calculator()
    memory = Memory()

    print("Вітаємо в калькуляторі")

    while True:
        print("\nВиберіть опцію:")
        print("1. Виконати обчислення")
        print("2. Використати операції з пам'яттю")
        print("3. Переглянути історію")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            operator = GetOperator()

            if operator == '√' or operator == 'sqrt':
                num = GetNumber()
                try:
                    result = calc.SquareRoot(num)
                except ValueError as e:
                    print(e)
                    continue
            else:
                num1 = GetNumber()
                num2 = GetNumber()

                try:
                    if operator == '+':
                        result = calc.Add(num1, num2)
                    elif operator == '-':
                        result = calc.Subtract(num1, num2)
                    elif operator == '*':
                        result = calc.Multiply(num1, num2)
                    elif operator == '/':
                        result = calc.Divide(num1, num2)
                    elif operator == '%':
                        result = calc.Mod(num1, num2)
                    elif operator == '**':
                        result = calc.Exponentiate(num1, num2)

                    print(f"Результат: {result}")

                except ValueError as e:
                    print(e)
                    continue

        elif choice == '2':
            print("\nОперації з пам'яттю:")
            print("1. Додати до пам'яті")
            print("2. Відняти з пам'яті")
            print("3. Очисити пам'ять")
            print("4. Прочитати пам'ять")

            mem_choice = input("Ваш вибір: ")

            if mem_choice == '1':
                value = GetNumber()
                result = memory.Add(value)
            elif mem_choice == '2':
                value = GetNumber()
                result = memory.Subtract(value)
            elif mem_choice == '3':
                result = memory.Clear()
            elif mem_choice == '4':
                result = memory.Read()

            print(f"Результат пам'яті: {result}")

        elif choice == '3':
            print("\nІсторія обчислень:")
            calc.GetHistory()

        elif choice == '4':
            print("На все добре!")
            break

        else:
            print("Невірний вибір. Будь ласка, виберіть правильну опцію.")


if __name__ == "__main__":
    main()