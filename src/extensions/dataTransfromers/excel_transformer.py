from models.sales_model import Sale
from models.special_values import  RawSaleColumnNames
import core.utility as utility 

class ExcelTransformer(): 
    
    def transformData(self,rawData) -> list[Sale]:
        transformedData = []
        for row in rawData:
            tRow = self._transformExcelRow(row)
            transformedData.append(tRow)
            
        return transformedData

    def _transformExcelRow(self,excelRow) :
        date = excelRow[RawSaleColumnNames.ORDERDATE]
        date = utility.strToDate(date)
        date = utility.dateToTimestamp(date)

        quantity = excelRow[RawSaleColumnNames.QUANTITYORDERED]
        sales = excelRow[RawSaleColumnNames.SALES]
        status = excelRow[RawSaleColumnNames.STATUS]
        product_code = excelRow[RawSaleColumnNames.PRODUCTCODE]
        state = excelRow[RawSaleColumnNames.STATE]
        country = excelRow[RawSaleColumnNames.COUNTRY]
        postal_code = excelRow[RawSaleColumnNames.POSTALCODE]

        return Sale(quantity,postal_code,sales,date,status,
    state,country,product_code)

    