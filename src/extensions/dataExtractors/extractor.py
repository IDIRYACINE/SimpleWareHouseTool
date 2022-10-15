from abc import ABC, abstractmethod

class Extractor(ABC) :

    @abstractmethod
    def exctract_data(startRow , rowsNumToExtract) :
        """Extract the data from the data source"""
        pass

    @abstractmethod
    def open_data_source() :
        """Open the data source"""
        pass

    @abstractmethod
    def close_data_source() :
        """Close the data source"""
        pass

    @abstractmethod
    def save_exctraction_progress() :
        """Save the extraction progress"""
        pass

    @abstractmethod
    def load_exctraction_progress() :
        """Load the extraction progress"""
        pass

    @abstractmethod
    def resume_extraction() :
        """Resume the extraction"""
        pass    
    
