import pyfiglet
from labs.lab3.UserInput.user_input import get_non_empty_input


def generate_ascii_art(text, font="slant"):
    return pyfiglet.figlet_format(text, font=font)

def choose_font():
    fonts = pyfiglet.FigletFont.getFonts()[:5]
    print("Доступні шрифти:")
    for i, font in enumerate(fonts, 1):
        print(f"{i}. {font}")
    choice = int(get_non_empty_input(f"Оберіть шрифт (1-{len(fonts)}): ")) - 1
    return fonts[choice]
