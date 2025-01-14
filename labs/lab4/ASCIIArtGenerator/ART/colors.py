colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    "dark_gray": "\033[38;5;8m",
    "light_gray": "\033[38;5;7m",
    "orange": "\033[38;5;214m",
    "purple": "\033[38;5;129m",
    "pink": "\033[38;5;205m",
    "lavender": "\033[38;5;183m",
    "olive": "\033[38;5;106m",
    "light_blue": "\033[38;5;81m",
    "aqua": "\033[38;5;51m",
    "light_green": "\033[38;5;120m",
    "pastel_pink": "\033[38;5;189m",
    "gold": "\033[38;5;220m",
    "silver": "\033[38;5;250m",
    "coral": "\033[38;5;210m",
    "cherry": "\033[38;5;9m",
    "lime": "\033[38;5;154m",
    "turquoise": "\033[38;5;49m",
    "mint": "\033[38;5;121m",
    "emerald": "\033[38;5;35m",
    "navy_blue": "\033[38;5;17m",
    "peach": "\033[38;5;215m",
    "salmon": "\033[38;5;209m",
    "sky_blue": "\033[38;5;153m",
    "light_cyan": "\033[38;5;195m",
    "dark_red": "\033[38;5;52m",
    "burgundy": "\033[38;5;88m",
    "mustard": "\033[38;5;3m",
    "violet": "\033[38;5;207m",
    "indigo": "\033[38;5;54m",
    "chocolate": "\033[38;5;130m",
    "rust": "\033[38;5;160m",
    "teal": "\033[38;5;30m",
    "fuchsia": "\033[38;5;13m",
    "light_purple": "\033[38;5;225m",
    "dark_blue": "\033[38;5;19m",
    "forest_green": "\033[38;5;22m",
    "goldenrod": "\033[38;5;178m",
    "neon_green": "\033[38;5;118m",
    "bronze": "\033[38;5;136m",
    "platinum": "\033[38;5;255m",
    "ivory": "\033[38;5;230m",
    "pearl": "\033[38;5;255m",
    "sand": "\033[38;5;228m",
    "charcoal": "\033[38;5;232m",
    "bright_orange": "\033[38;5;202m",
}

def get_color_code(color_name):
    return colors.get(color_name, "\033[0m")

