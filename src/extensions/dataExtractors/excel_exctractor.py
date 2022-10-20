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
        rowsIterator = worksheet.iter_rows(min_row=startRow, max_row=rowsNumToExtract + startRow, values_only=True)
        
        extractedData : list[Sale] = []

        rowExcelIndex = startRow
        for row in rowsIterator :
            extractedRow = self._extractCellsFromRow(row,rowExcelIndex)
            extractedData.append(extractedRow)
            rowExcelIndex = rowExcelIndex + 1

        return self._transformer.transformData(extractedData)    

    def open_data_source(self,dataSourcePath) :
        self._workBook =  load_workbook(dataSourcePath , read_only=True)

    def close_data_source(self) :
        self._workBook.close()

    def _extractCellsFromRow(self,row,rowIndex) :
        extractedRow = {}
        for column in self._columns :
            cellId = column+rowIndex
            columnName = ExcelDataColumnsDict[column]
            extractedRow[columnName] = row[cellId]
        return extractedRow
        

