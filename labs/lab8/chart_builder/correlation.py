import matplotlib.pyplot as plt
import seaborn as sns
from .base import ChartBuilder

class CorrelationMatrixBuilder(ChartBuilder):
    def build_chart(self, data):
        correlation_matrix = data.corr()
        fig = plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title("Кореляційна матриця")
        return fig
