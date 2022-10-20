from abc import ABC, abstractmethod
from models.sales_model import Sale 

class Extractor(ABC) :

    @abstractmethod
    def extract_data(self,startRow , rowsNumToExtract) -> list[Sale] :
        """Extract the data from the data source"""
        pass

    @abstractmethod
    def open_data_source(dataSourcePath) :
        """Open the data source"""
        pass

    @abstractmethod
    def close_data_source(self) :
        """Close the data source"""
        pass

    
