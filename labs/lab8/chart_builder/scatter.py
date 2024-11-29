import matplotlib.pyplot as plt
from .base import ChartBuilder

class ScatterPlotBuilder(ChartBuilder):
    def build_chart(self, data):
        fig = plt.figure(figsize=(8, 6))
        plt.scatter(data['alcohol'], data['quality'], alpha=0.5, color='red')
        plt.title("Залежність між вмістом алкоголю та якістю вина")
        plt.xlabel("Вміст алкоголю (%)")
        plt.ylabel("Якість вина")
        return fig
