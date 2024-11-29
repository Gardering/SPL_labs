from labs.lab8.wine_visualizer import WineVisualizer

class Lab8Facade:
    def __init__(self):
        self.visualizer = WineVisualizer()

    def execute(self):
        print("=== Лабораторна робота 8: Візуалізація даних про вино ===")
        self.visualizer.start()
