import extensions.dataExtractors.data_extractor as data_extractor
import pandas as pd
from extensions.dataTransfromers.csv_transformer import CsvTransformer
from models.sales_model import Sale

class CsvExtractor(data_extractor.Extractor) :

    def __init__(self,columnsNames) :
        self._columnsNames = columnsNames
        self._transformer = CsvTransformer()
        

    def extract_data(self,startRow, rowsNumToExtract) -> list[Sale] :
        if(self._dataSourceFile == None) :
            return None
        extracted_data =  pd.read_csv(
            self._dataSourceFile, 
            nrows=rowsNumToExtract,
            skiprows=startRow,
            usecols = self._columnsNames
        )

        return self._transformer.transformData(extracted_data)
        
    def open_data_source(self,dataSourcePath) :
        self._dataSourceFile = dataSourcePath

    def close_data_source(self) :
        self._dataSourceFile = None
        pass
