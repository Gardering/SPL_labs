import os

def save_to_file(ascii_art):
    if not os.path.exists("../ARTTXT"):
        os.makedirs("../ARTTXT")
    filename = input("Введіть ім'я файлу (без розширення): ") + ".txt"
    filepath = os.path.join("../ARTTXT", filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл: {filepath}")
