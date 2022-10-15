from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def generate_sales_summary():
        pass