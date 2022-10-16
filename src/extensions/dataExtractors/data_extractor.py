from abc import ABC, abstractmethod

class Extractor(ABC) :

    @abstractmethod
    def extract_data(self,startRow , rowsNumToExtract) :
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

    @abstractmethod
    def save_extraction_progress() :
        """Save the extraction progress"""
        pass

    @abstractmethod
    def load_extraction_progress() :
        """Load the extraction progress"""
        pass

    @abstractmethod
    def resume_extraction() :
        """Resume the extraction"""
        pass    
    
