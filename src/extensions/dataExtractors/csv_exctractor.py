import imp


import extractor

class CsvExtractor(extractor.Extractor) :
    _dataSourcePath = None

    def __init__(self, dataSourcePath) :
        self._dataSourcePath = dataSourcePath

    def extract_data(startRow, rowsNumToExtract) :
        """Extract the data from the data source"""
        pass

    def open_data_source(self) :
        """Open the data source"""
        pass

    def close_data_source(self) :
        """Close the data source"""
        pass

    def save_extraction_progress(self) :
        """Save the extraction progress"""
        pass

    def load_extraction_progress(self) :
        """Load the extraction progress"""
        pass

    def resume_extraction(self) :
        """Resume the extraction"""
        pass