import os


def display_ascii_art(ascii_art, color, alignment='left'):
    lines = ascii_art.split('\n')

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    if alignment == 'center':
        for line in lines:
            print(f"{color}" + line.center(terminal_width) + "\033[0m")
    elif alignment == 'right':
        for line in lines:
            print(f"{color}" + line.rjust(terminal_width) + "\033[0m")
    else:
        for line in lines:
            print(f"{color}" + line + "\033[0m")
