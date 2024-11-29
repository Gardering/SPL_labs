from labs.lab5.pythonProject1.shapes.cube import Cube
from labs.lab5.pythonProject1.shapes.pyramid import Pyramid
from labs.lab5.pythonProject1.utils.color_loader import load_colors_from_json
from labs.lab5.pythonProject1.utils.file_operations import save_to_file
from labs.lab5.pythonProject1.utils.user_input import (get_shape_type, get_scale_factor, get_rotation_direction, get_color_choice, get_save_prompt, get_filename)
import numpy as np

class Lab5Facade:

    def execute(self):
        angle_x = 0
        angle_y = 0
        current_size = 1.5

        colors, default_color = load_colors_from_json()

        shape_type = get_shape_type()
        shape = Cube(current_size, default_color) if shape_type == "cube" else Pyramid(current_size, default_color)

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
