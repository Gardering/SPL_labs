from labs.lab3.UserInput.user_input import get_non_empty_input

def choose_symbols():
    symbols = get_non_empty_input("Введіть символи для використання в ASCII-арті (за замовчуванням '#'): ")
    if not symbols:
        symbols = '#'
    return symbols
