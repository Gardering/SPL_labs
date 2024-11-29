import numpy as np

class Shape:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.reset_color = "\033[0m"

    def get_vertices(self):
        raise NotImplementedError("Метод get_vertices() повинен бути реалізований у підкласах.")

    def get_edges(self):
        raise NotImplementedError("Метод get_edges() повинен бути реалізований у підкласах.")

    def draw(self, angle_x, angle_y):
        vertices = self.get_vertices()
        edges = self.get_edges()

        rotated_vertices = [self.rotate(v, angle_x, angle_y) for v in vertices]
        projected_vertices = [self.project(v) for v in rotated_vertices]

        canvas = [[' ' for _ in range(40)] for _ in range(20)]
        for start, end in edges:
            x1, y1 = projected_vertices[start]
            x2, y2 = projected_vertices[end]
            char = '+' if isinstance(self, Cube) and start in {0, 4} and end in {1, 5} else '#'
            self.draw_line(canvas, x1, y1, x2, y2, char)

        return "\n".join("".join(line) for line in canvas)

    def rotate(self, vertex, angle_x, angle_y):
        rotation_x = np.array([
            [1, 0, 0],
            [0, np.cos(angle_x), -np.sin(angle_x)],
            [0, np.sin(angle_x), np.cos(angle_x)]
        ])
        rotation_y = np.array([
            [np.cos(angle_y), 0, np.sin(angle_y)],
            [0, 1, 0],
            [-np.sin(angle_y), 0, np.cos(angle_y)]
        ])
        return rotation_y @ rotation_x @ vertex

    def project(self, vertex):
        x = int(vertex[0] + 20)
        y = int(vertex[1] + 8)
        return x, y

    def draw_line(self, canvas, x1, y1, x2, y2, char='#'):
        dx, dy = x2 - x1, y2 - y1
        steps = max(abs(dx), abs(dy)) + 1
        for i in range(steps):
            x = int(x1 + i * dx / steps)
            y = int(y1 + i * dy / steps)
            if 0 <= x < 40 and 0 <= y < 20:
                canvas[y][x] = f"{self.color}{char}{self.reset_color}"


class Cube(Shape):
    def get_vertices(self):
        return np.array([
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ]) * self.size

    def get_edges(self):
        return [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]


class Pyramid(Shape):
    def get_vertices(self):
        return np.array([
            [0, -1, 0],
            [-1, 0, -1],
            [1, 0, -1],
            [1, 0, 1],
            [-1, 0, 1]
        ]) * self.size

    def get_edges(self):
        return [
            (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 2), (2, 3), (3, 4), (4, 1)
        ]
