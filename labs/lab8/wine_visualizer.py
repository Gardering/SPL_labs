import os
from labs.lab8.data_handler import DataHandler
from labs.lab8.chart_saver import ChartSaver
from labs.lab8.user_input import UserInput
from labs.lab8.chart_builder.histogram import HistogramBuilder
from labs.lab8.chart_builder.scatter import ScatterPlotBuilder
from labs.lab8.chart_builder.correlation import CorrelationMatrixBuilder
from labs.lab8.chart_builder.multiple import MultipleSubplotsBuilder


class WineVisualizer:
    def __init__(self):
        self.data_handler = DataHandler()  # Ініціалізуємо data_handler
        self.chart_saver = ChartSaver()

    def start(self):
        while True:
            wine_type = UserInput.input_non_empty("Виберіть тип вина (red для червоного, white для білого): ",
                                                  valid_choices=['red', 'white'])

            # Динамічно визначаємо шлях до файлу
            base_dir = os.path.dirname(os.path.abspath(__file__))  # Базова директорія (labs/lab8)
            file_path = os.path.join(base_dir, 'csv', f'winequality-{wine_type}.csv')

            try:
                data = self.data_handler.load_data(file_path)
            except FileNotFoundError:
                print(f"Файл {file_path} не знайдено. Переконайтесь, що файли CSV існують.")
                continue

            print(data.head())
            print(data.info())

            self._show_chart_options(data)

            another_wine = UserInput.input_non_empty("\nХочете вибрати інший тип вина (y/n)? ", valid_choices=['y', 'n'])
            if another_wine != 'y':
                break

    def _show_chart_options(self, data):
        chart_builders = {
            '1': HistogramBuilder(),
            '2': ScatterPlotBuilder(),
            '3': CorrelationMatrixBuilder(),
            '4': MultipleSubplotsBuilder()
        }

        while True:
            print("\nВиберіть тип діаграми для побудови:")
            print("1. Гістограма для розподілу якості вина")
            print("2. Діаграма розсіювання для залежності алкоголю та якості вина")
            print("3. Кореляційна матриця")
            print("4. Кілька піддіаграм")
            print("5. Вийти")

            chart_choice = UserInput.input_non_empty("\nВведіть номер діаграми (1-5): ", valid_choices=['1', '2', '3', '4', '5'])

            if chart_choice == '5':
                print("Вихід з програми.")
                return

            chart_builder = chart_builders.get(chart_choice)
            if chart_builder:
                fig = chart_builder.build_chart(data)
                self.chart_saver.save_chart(fig)

            continue_choice = UserInput.input_non_empty("\nХочете вибрати іншу діаграму (y/n)? ", valid_choices=['y', 'n'])
            if continue_choice != 'y':
                break
