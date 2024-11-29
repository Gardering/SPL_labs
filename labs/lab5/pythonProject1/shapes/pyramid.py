import numpy as np
from labs.lab5.pythonProject1.shapes.shape import Shape

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
