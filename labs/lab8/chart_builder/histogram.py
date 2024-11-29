import matplotlib.pyplot as plt
from .base import ChartBuilder

class HistogramBuilder(ChartBuilder):
    def build_chart(self, data):
        fig = plt.figure(figsize=(8, 6))
        plt.hist(data['quality'], bins=range(3, 10), edgecolor='black', color='skyblue')
        plt.title("Розподіл якості вин")
        plt.xlabel("Якість вина")
        plt.ylabel("Кількість")
        plt.xticks(range(3, 10))
        return fig
