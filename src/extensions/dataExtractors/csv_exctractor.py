import extensions.dataExtractors.data_extractor as data_extractor , pandas as pd

class CsvExtractor(data_extractor.Extractor) :

    def __init__(self,columnsNames) :
        self._columnsNames = columnsNames
        

    def extract_data(self,startRow, rowsNumToExtract) :
        if(self._dataSourceFile == None) :
            return None
        self.extract_data =  pd.read_csv(
            self._dataSourceFile, 
            nrows=rowsNumToExtract,
            skiprows=startRow,
            usecols = self._columnsNames
        )

        return self.extract_data
        
    def open_data_source(self,dataSourcePath) :
        self._dataSourceFile = dataSourcePath

    def close_data_source(self) :
        self._dataSourceFile = None
        pass

    def save_extraction_progress() :
        """Save the extraction progress"""
        pass

    def load_extraction_progress() :
        """Load the extraction progress"""
        pass

    def resume_extraction() :
        """Resume the extraction"""
        pass