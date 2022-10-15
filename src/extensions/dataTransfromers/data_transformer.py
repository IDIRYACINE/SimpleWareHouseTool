from abc import ABC, abstractmethod

class DataTransformer(ABC):

    @abstractmethod
    def transformData(rawData):
        pass
