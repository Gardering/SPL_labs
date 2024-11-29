from labs.lab3.ARTGeneration.art_generation import generate_ascii_art, choose_font
from labs.lab3.ARTGeneration.colors import choose_color
from labs.lab3.ARTGeneration.file_operations import save_to_file
from labs.lab3.ARTGeneration.size_selection import scale_ascii_art, replace_with_symbols
from labs.lab3.ARTGeneration.symbols_selection import choose_symbols
from labs.lab3.UserInput.user_input import get_user_input, choose_size
from labs.lab3.UserInput.formatting import format_ascii_art, choose_alignment
from termcolor import colored

class Lab3Facade:

    def __init__(self):
        self.text = None
        self.font = None
        self.color = None
        self.alignment = None
        self.max_width = None
        self.max_height = None
        self.symbols = None
        self.ascii_art = None
        self.formatted_ascii_art = None
        self.colored_ascii_art = None
        self.scaled_ascii_art = None
        self.custom_ascii_art = None

    def gather_input(self):
        self.text = get_user_input()
        self.font = choose_font()
        self.color = choose_color()
        self.alignment = choose_alignment()

    def generate_ascii(self):
        self.ascii_art = generate_ascii_art(self.text, font=self.font)
        self.colored_ascii_art = colored(self.ascii_art, self.color)
        self.formatted_ascii_art = format_ascii_art(self.colored_ascii_art, self.alignment)

    def scale_and_customize(self):
        self.max_width, self.max_height = choose_size()
        self.scaled_ascii_art = scale_ascii_art(self.formatted_ascii_art, self.max_width, self.max_height)
        self.symbols = choose_symbols()
        self.custom_ascii_art = replace_with_symbols(self.scaled_ascii_art, self.symbols)

    def preview_and_save(self):
        print("\nПопередній перегляд ASCII-арту:")
        print(self.custom_ascii_art)

        user_choice = input("\n Введіть 'y' для продовження або 'n' для перезапуску: ").strip().lower()

        if user_choice == 'y':
            save_option = input("Зберегти ASCII-арт у файл? (y/n): ").lower()
            if save_option == 'y':
                save_to_file(self.custom_ascii_art)
        else:
            print("Процес перезапускається...")

    def execute(self):
        self.gather_input()
        self.generate_ascii()
        self.scale_and_customize()
        self.preview_and_save()
