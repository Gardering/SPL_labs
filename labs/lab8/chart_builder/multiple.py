import matplotlib.pyplot as plt
import seaborn as sns
from .base import ChartBuilder

class MultipleSubplotsBuilder(ChartBuilder):
    def build_chart(self, data):
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        axes[0, 0].hist(data['alcohol'], bins=20, edgecolor='black', color='skyblue')
        axes[0, 0].set_title('Розподіл вмісту алкоголю')
        axes[0, 0].set_xlabel('Вміст алкоголю (%)')
        axes[0, 0].set_ylabel('Частота')

        axes[0, 1].scatter(data['alcohol'], data['quality'], alpha=0.5, color='red')
        axes[0, 1].set_title('Залежність між алкоголем та якістю')
        axes[0, 1].set_xlabel('Вміст алкоголю (%)')
        axes[0, 1].set_ylabel('Якість вина')

        axes[1, 0].hist(data['quality'], bins=range(3, 10), edgecolor='black', color='lightgreen')
        axes[1, 0].set_title('Розподіл якості вина')
        axes[1, 0].set_xlabel('Якість вина')
        axes[1, 0].set_ylabel('Частота')

        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=axes[1, 1])
        axes[1, 1].set_title('Кореляційна матриця')

        plt.tight_layout()
        return fig
