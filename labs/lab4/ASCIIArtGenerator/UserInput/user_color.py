from labs.lab4.ASCIIArtGenerator.ART.colors import get_color_code, colors

def get_color():
    while True:
        color_choice = input("Оберіть колір для вашого арту: ").strip().lower()
        if color_choice in colors:
            return get_color_code(color_choice)
        else:
            print("Помилка. Виберіть один з доступних кольорів.")
