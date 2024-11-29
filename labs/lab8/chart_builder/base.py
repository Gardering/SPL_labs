from abc import ABC, abstractmethod

class ChartBuilder(ABC):
    @abstractmethod
    def build_chart(self, data):
        pass
