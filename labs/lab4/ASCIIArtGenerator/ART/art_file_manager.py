import os

def save_ascii_art_to_file(ascii_art):
    if not os.path.exists("ARTTXT"):
        os.makedirs("ARTTXT")

    while True:
        filename = input("Введіть ім'я файлу для збереження (без розширення): ").strip()
        if filename:
            filepath = os.path.join("ARTTXT", f"{filename}.txt")

            try:
                with open(filepath, "w") as file:
                    file.write(ascii_art)
                print(f"Ваш ASCII-арт збережено у файл: {filepath}")
                break
            except Exception as e:
                print(f"Помилка при збереженні файлу: {e}. Спробуйте ще раз.")
        else:
            print("Ім'я файлу не може бути порожнім. Будь ласка, введіть ім'я файлу.")
