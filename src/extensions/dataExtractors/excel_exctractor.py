import extensions.dataExtractors.data_extractor as data_extractor
from openpyxl import load_workbook
from models.sales_model import Sale
from models.special_values import ExcelDataColumnsDict
from extensions.dataTransfromers.excel_transformer import ExcelTransformer

class ExcelExtractor(data_extractor.Extractor) :

    def __init__(self,columnsNames) :
        self._columns = columnsNames
        self._transformer = ExcelTransformer()

    def extract_data(self,sheetName :str, startRow, rowsNumToExtract) -> list[Sale] :
        worksheet = self._workBook[sheetName]
        
        extractedData : list[Sale] = []

        for rowIndex in range(startRow,rowsNumToExtract ):
            extractedRow = self._extractCellsFromRow(worksheet,rowIndex)
            extractedData.append(extractedRow)

        return self._transformer.transformData(extractedData)    

    def open_data_source(self,dataSourcePath) :
        self._workBook =  load_workbook(dataSourcePath , read_only=True)

    def close_data_source(self) :
        self._workBook.close()

    def _extractCellsFromRow(self,worksheet,rowIndex) :

        extractedRow = {}
        for column in self._columns :
            excelColumnName = ExcelDataColumnsDict[column]
            cellId = "{0}{1}".format(excelColumnName , rowIndex)
            extractedRow[column.value] = worksheet[cellId].value

        return extractedRow
        

