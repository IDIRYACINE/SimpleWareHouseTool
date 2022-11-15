import extensions.dataExtractors.data_extractor as data_extractor
import pandas as pd
from extensions.dataTransfromers.csv_transformer import CsvTransformer
from models.sales_model import Sale

class CsvExtractor(data_extractor.Extractor) :

    def __init__(self,columnsNames : list) :
        self._columnsNames = [column.value for column in columnsNames]
        self._transformer = CsvTransformer()
        

    def extract_data(self, sheetName ,startRow, rowsNumToExtract) -> list[Sale] :
        if(self._dataSourceFile == None) :
            return None
      
        extracted_data =  pd.read_csv(
            self._dataSourceFile, 
            sep=',',
            usecols = self._columnsNames,
            nrows=rowsNumToExtract ,
            skiprows=[startRow],
        )

        return self._transformer.transformData(extracted_data)
        
    def open_data_source(self,dataSourcePath) :
        self._dataSourceFile = dataSourcePath

    def close_data_source(self) :
        self._dataSourceFile = None
        pass
