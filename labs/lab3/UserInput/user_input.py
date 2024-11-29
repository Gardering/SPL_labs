def get_non_empty_input(prompt):
    user_input = input(prompt).strip()
    while not user_input:
        print("Помилка: Введення не може бути порожнім.")
        user_input = input(prompt).strip()
    return user_input

def get_user_input():
    return get_non_empty_input("Введіть слово або фразу для перетворення в ASCII-арт: ")

def choose_size():
    while True:
        try:
            max_width = int(get_non_empty_input("Введіть максимальну ширину ASCII-арту (або 0 для автоматичної): "))
            max_height = int(get_non_empty_input("Введіть максимальну висоту ASCII-арту (або 0 для автоматичної): "))
            if max_width < 0 or max_height < 0:
                print("Помилка значення повинні бути невід'ємними.")
                continue
            break
        except ValueError:
            print("Помилка, введіть числові значення.")

    if max_width == 0:
        max_width = None
    if max_height == 0:
        max_height = None

    print(f"Оберені параметри: Ширина - {max_width}, Висота - {max_height}")
    return max_width, max_height
