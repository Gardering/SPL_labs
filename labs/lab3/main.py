from termcolor import colored
from labs.lab3.UserInput.user_input import get_user_input, choose_size, get_non_empty_input
from labs.lab3.ARTGeneration.art_generation import generate_ascii_art, choose_font
from labs.lab3.UserInput.formatting import format_ascii_art, choose_alignment
from labs.lab3.ARTGeneration.colors import choose_color
from labs.lab3.ARTGeneration.file_operations import save_to_file
from labs.lab3.ARTGeneration.size_selection import scale_ascii_art, replace_with_symbols
from labs.lab3.ARTGeneration.symbols_selection import choose_symbols


def preview_ascii_art(ascii_art):
    print("\nПопередній перегляд ASCII-арту:")
    print(ascii_art)

    print(colored("", "white"))

    while True:
        choice = input("\n Введіть 'y' для продовження або 'n' для перезапуску: ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Неправильний ввід. Введіть 'y' або 'n.")


def main():
    while True:
        print("___ ASCII ARTTXT Генератор ___")
        text = get_user_input()
        font = choose_font()
        color = choose_color()
        alignment = choose_alignment()

        ascii_art = generate_ascii_art(text, font=font)
        colored_ascii_art = colored(ascii_art, color)
        formatted_ascii_art = format_ascii_art(colored_ascii_art, alignment)

        max_width, max_height = choose_size()
        scaled_ascii_art = scale_ascii_art(formatted_ascii_art, max_width, max_height)

        symbols = choose_symbols()
        custom_ascii_art = replace_with_symbols(scaled_ascii_art, symbols)

        user_choice = preview_ascii_art(custom_ascii_art)

        if user_choice == 'почати заново':
            continue
        else:
            save_option = get_non_empty_input(" Зберегти ASCII-арт у файл? (y/n): ").lower()
            if save_option == "y":
                save_to_file(custom_ascii_art)

        break


if __name__ == "__main__":
    main()