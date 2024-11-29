import os
import mpld3
import matplotlib.pyplot as plt
from labs.lab8.user_input import UserInput


class ChartSaver:
    @staticmethod
    def save_chart(chart):
        plt.show()

        save_choice = UserInput.input_non_empty("Бажаєте зберегти діаграму? (y/n): ", valid_choices=['y', 'n'])
        if save_choice == 'y':
            file_format = UserInput.input_non_empty(
                "Виберіть формат для збереження (png, jpg, svg, pdf, html): ",
                valid_choices=['png', 'jpg', 'svg', 'pdf', 'html']
            )
            file_name = UserInput.input_non_empty("Введіть назву файлу (без розширення): ")

            if not os.path.exists('charts'):
                os.makedirs('charts')

            if file_format == 'html':
                html_file = f'charts/{file_name}.html'
                mpld3.save_html(chart, html_file)
            else:
                chart.savefig(f'charts/{file_name}.{file_format}', format=file_format)

        plt.close(chart)
