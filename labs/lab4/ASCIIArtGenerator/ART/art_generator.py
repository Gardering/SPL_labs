from labs.lab4.ASCIIArtGenerator.ART.colors import get_color_code, colors
from labs.lab4.ASCIIArtGenerator.ART.ascii_library import print_ascii_art

def generate_ascii_art(text, symbol):
    return print_ascii_art(text, symbol)

def get_art_color():
    while True:
        color_choice = input("Оберіть колір для вашого арту: ").strip().lower()
        if color_choice in colors:
            return get_color_code(color_choice)
        else:
            print("Помилка. Виберіть один з доступних кольорів.")
