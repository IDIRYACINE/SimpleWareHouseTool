import datetime
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
        
        date = excelRow[RawSaleColumnNames.ORDERDATE.value]
        if(isinstance(date,str)):
            date = utility.strToDate(date)

        hour = '{0}.{1}'.format(date.hour,date.minute)
        date = datetime.date(date.year,date.month,date.day)

        quantity = excelRow[RawSaleColumnNames.QUANTITYORDERED.value]
        sales = excelRow[RawSaleColumnNames.SALES.value]

        status = excelRow[RawSaleColumnNames.STATUS.value]
        status = utility.statusToCode(status)

        product_code = excelRow[RawSaleColumnNames.PRODUCTCODE.value]
        state = excelRow[RawSaleColumnNames.STATE.value]
        country = excelRow[RawSaleColumnNames.COUNTRY.value]
        postal_code = excelRow[RawSaleColumnNames.POSTALCODE.value]

        return Sale(quantity,postal_code,sales,date,status,
    state,country,product_code)

    