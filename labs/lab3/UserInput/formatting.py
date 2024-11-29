import os
from labs.lab3.UserInput.user_input import get_non_empty_input


def format_ascii_art(ascii_art, alignment="center"):
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80

    lines = ascii_art.splitlines()

    if alignment == "center":
        formatted_art = "\n".join(line.center(width) for line in lines)
    elif alignment == "left":
        formatted_art = "\n".join(line.ljust(width) for line in lines)
    elif alignment == "right":
        formatted_art = "\n".join(line.rjust(width) for line in lines)
    else:
        formatted_art = ascii_art

    return formatted_art


def choose_alignment():
    alignments = ["left", "center", "right"]
    print("Вирівнювання:")
    for i, align in enumerate(alignments, 1):
        print(f"{i}. {align}")
    choice = int(get_non_empty_input(f"Оберіть вирівнювання (1-{len(alignments)}): ")) - 1
    return alignments[choice]