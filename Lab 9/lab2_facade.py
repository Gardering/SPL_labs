from labs.lab2.classes.calculator import Calculator, Memory

class Lab2Facade:
    """
    Клас, що представляє фасад для взаємодії з калькулятором та пам'яттю.
    Забезпечує меню для вибору операцій калькулятора, роботи з історією обчислень та пам'яттю.

    Атрибути:
        calculator (Calculator): Об'єкт калькулятора для виконання математичних операцій.
        memory (Memory): Об'єкт пам'яті для збереження значень.
    """

    def __init__(self):
        """
        Ініціалізація фасаду, створення об'єктів калькулятора та пам'яті.
        """
        self.calculator = Calculator()
        self.memory = Memory()

    def calculator_menu(self):
        """
        Меню калькулятора, яке дозволяє користувачеві вибирати операції, переглядати історію обчислень
        та взаємодіяти з пам'яттю.

        Виконується в циклі, поки користувач не вибере "Назад".
        """
        while True:
            print("\n=== Калькулятор ===")
            print("1. Робота з операціями")
            print("2. Історія обчислень")
            print("3. Робота з пам'яттю")
            print("0. Назад")

            choice = input("Ваш вибір: ").strip()
            if choice == '0':
                break

            if choice == '1':
                self.operation_menu()

            elif choice == '2':
                history = self.calculator.GetHistory()
                print("Історія обчислень:")
                for record in history:
                    print(record)
            elif choice == '3':
                self.memory_menu()
            else:
                print("Неправильний вибір, спробуйте ще раз.")

    def operation_menu(self):
        """
        Меню для вибору математичних операцій, таких як додавання, віднімання, множення, ділення, тощо.

        Запитує у користувача два числа та виконує обрану операцію.
        """
        print("\n=== Операції ===")
        print("1. Додавання (+)")
        print("2. Віднімання (-)")
        print("3. Множення (*)")
        print("4. Ділення (/)")
        print("5. Модульне ділення (%)")
        print("6. Піднесення до степеня (^)")
        print("7. Корінь квадратний (sqrt)")

        operation_choice = input("Виберіть операцію: ").strip()

        if operation_choice in {'1', '2', '3', '4', '5', '6'}:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            operations = {
                '1': self.calculator.Add,
                '2': self.calculator.Subtract,
                '3': self.calculator.Multiply,
                '4': self.calculator.Divide,
                '5': self.calculator.Mod,
                '6': self.calculator.Exponentiate,
            }
            result = operations[operation_choice](a, b)
            print(f"Результат: {result}")
        elif operation_choice == '7':
            number = float(input("Введіть число: "))
            result = self.calculator.SquareRoot(number)
            print(f"Корінь квадратний: {result}")
        else:
            print("Неправильний вибір операції, спробуйте ще раз.")

    def memory_menu(self):
        """
        Меню для роботи з пам'яттю, яке дозволяє додавати або віднімати значення з пам'яті,
        переглядати поточні значення та очищати пам'ять.

        Виконується в циклі, поки користувач не вибере "Назад".
        """
        while True:
            print("\n=== Робота з пам'яттю ===")
            print("1. Додати до пам'яті")
            print("2. Відняти з пам'яті")
            print("3. Переглянути пам'ять")
            print("4. Очистити пам'ять")
            print("0. Назад")

            choice = input("Ваш вибір: ").strip()
            if choice == '0':
                break

            if choice == '1':
                value = float(input("Введіть значення для додавання: "))
                self.memory.Add(value)
            elif choice == '2':
                value = float(input("Введіть значення для віднімання: "))
                self.memory.Subtract(value)
            elif choice == '3':
                print(f"Значення в пам'яті: {self.memory.Read()}")
            elif choice == '4':
                self.memory.Clear()
                print("Пам'ять очищено.")
            else:
                print("Неправильний вибір, спробуйте ще раз.")

    def execute(self):
        """
        Запуск основного меню калькулятора.

        Ця функція ініціює запуск калькулятора.
        """
        self.calculator_menu()
