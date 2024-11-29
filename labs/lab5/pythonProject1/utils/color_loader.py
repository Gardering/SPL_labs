import json
import os

def load_colors_from_json():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    try:
        with open(config_path, 'r') as file:
            data = json.load(file)
            colors = data.get("colors", {})
            default_color_name = data.get("default_color", "white")
            color = colors.get(default_color_name, colors.get("white", "\033[37m"))
            return colors, color
    except FileNotFoundError:
        print("Файл config.json не знайдено. Використовується колір за замовчуванням (білий).")
        return {"white": "\033[37m"}, "\033[37m"
