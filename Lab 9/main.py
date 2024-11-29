"""
Головний модуль програми, який забезпечує взаємодію з користувачем через головне меню.
Користувач може вибирати лабораторні роботи для виконання через відповідні фасади.
Програма працює в циклі до вибору опції "Вихід", після чого завершується.
"""

from lab1_facade import Lab1Facade
from lab2_facade import Lab2Facade
from lab3_facade import Lab3Facade
from lab4_facade import Lab4Facade
from lab5_facade import Lab5Facade
from lab7_facade import Lab7Facade
from lab8_facade import Lab8Facade

def main():
    """
    Основне меню програми, яке дозволяє користувачеві вибрати лабораторну роботу для виконання.
    Кожна лабораторна робота виконується через відповідний фасад.

    Меню працює в циклі, доки користувач не вибере опцію "Вихід".
    """
    while True:
        print("\n=== Головне меню ===")
        print("1. Лабораторна 1: Консольний калькулятор")
        print("2. Лабораторна 2: Калькулятор")
        print("3. Лабораторна 3: Генерація ASCII-арту")
        print("4. Лабораторна 4: Генерація та збереження ASCII-арту")
        print("5. Лабораторна 5: Обертання, зміна масштабу і збереження форм")
        print("6. Лабораторна 6: Виконання тестів")
        print("7. Лабораторна 7: Робота з API, збереження даних та журналювання")
        print("8. Лабораторна 8: Візуалізація вина")
        print("0. Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == '0':
            print("Дякуємо за використання програми!")
            break

        elif choice == '1':
            lab1_facade = Lab1Facade()
            lab1_facade.execute()

        elif choice == '2':
            lab2_facade = Lab2Facade()
            lab2_facade.execute()

        elif choice == '3':
            lab3_facade = Lab3Facade()
            lab3_facade.execute()

        elif choice == '4':
            lab4_facade = Lab4Facade()
            lab4_facade.execute()

        elif choice == '5':
            lab5_facade = Lab5Facade()
            lab5_facade.execute()

        elif choice == '7':
            lab7_facade = Lab7Facade()
            lab7_facade.execute()

        elif choice == '8':
            lab8_facade = Lab8Facade()
            lab8_facade.execute()

        else:
            print("Неправильний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
