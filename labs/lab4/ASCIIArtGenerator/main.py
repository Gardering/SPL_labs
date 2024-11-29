from labs.lab4.ASCIIArtGenerator.ART.art_generator import generate_ascii_art, get_art_color
from labs.lab4.ASCIIArtGenerator.ART.art_display import display_ascii_art
from labs.lab4.ASCIIArtGenerator.ART.art_file_manager import save_ascii_art_to_file
from labs.lab4.ASCIIArtGenerator.UserInput.user_text import get_user_text
from labs.lab4.ASCIIArtGenerator.UserInput.user_symbol import get_symbol_set
from labs.lab4.ASCIIArtGenerator.UserInput.user_dimensions import get_dimensions
from labs.lab4.ASCIIArtGenerator.UserInput.user_text import get_alignment_choice

def print_intro():
    print("-----Генератор ASCII-арту!-----")

if __name__ == "__main__":
    print_intro()

    while True:
        text = get_user_text()
        symbol = get_symbol_set()
        width, height = get_dimensions()
        color = get_art_color()
        alignment = get_alignment_choice()
        ascii_art = generate_ascii_art(text, symbol)
        display_ascii_art(ascii_art, color, alignment)

        while True:
            choice = input("Бажаєте змінити колір чи символ арту? (color / symbol / save): ").strip().lower()

            if choice == "color":
                color = get_art_color()
                display_ascii_art(ascii_art, color, alignment)

            elif choice == "symbol":
                symbol = get_symbol_set()
                ascii_art = generate_ascii_art(text, symbol)
                display_ascii_art(ascii_art, color, alignment)

            elif choice == "save":
                save_ascii_art_to_file(ascii_art)
                break

            else:
                print("Неправильний вибір. Будь ласка, виберіть 'color', 'symbol' або 'save'.")

        while True:
            another = input("Створити ще один ASCII-арт? (y/n): ").strip().lower()
            if another:
                break
            else:
                print("Введення не може бути порожнім. Будь ласка, введіть 'y' або 'n'.")

        if another != "y":
            break