from shapes.cube import Cube
from shapes.pyramid import Pyramid
from utils.color_loader import load_colors_from_json
from utils.file_operations import save_to_file
from utils.user_input import (get_shape_type, get_scale_factor, get_rotation_direction, get_color_choice,get_save_prompt, get_filename)
import numpy as np

def main():
    angle_x = 0
    angle_y = 0
    current_size = 1.5

    colors, color = load_colors_from_json()

    shape_type = get_shape_type()
    shape = Cube(current_size, color) if shape_type == "cube" else Pyramid(current_size, color)

    shape_representation = shape.draw(angle_x, angle_y)
    print(shape_representation)

    while True:
        scale_factor = get_scale_factor()
        if scale_factor == 'exit':
            print("Вихід з програми.")
            break

        current_size *= scale_factor
        shape.size = current_size

        direction = get_rotation_direction()
        if direction == 'top':
            angle_x -= np.radians(15)
        elif direction == 'bottom':
            angle_x += np.radians(15)
        elif direction == 'left':
            angle_y -= np.radians(15)
        elif direction == 'right':
            angle_y += np.radians(15)

        color_choice = get_color_choice(colors)
        if color_choice:
            shape.color = colors[color_choice]

        shape_representation = shape.draw(angle_x, angle_y)
        print(shape_representation)

        save_prompt = get_save_prompt()
        if save_prompt == 'y':
            filename = get_filename()
            save_to_file(filename, shape_representation.replace(f"{shape.color}", "").replace("\033[0m", ""))
            print(f"Фігуру збережено у файл {filename}.")

if __name__ == "__main__":
    main()