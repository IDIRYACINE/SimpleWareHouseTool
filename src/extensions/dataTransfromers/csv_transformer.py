from core import utility
import pandas as pd
from models import sales_model
import datetime

class CsvTransformer(): 

    def transformData(self,rawData : pd.DataFrame):
        transformedData = []
        print(rawData.head())
        for row in rawData.itertuples():
            tRow = self._transformCsvRow(row)
            transformedData.append(tRow)
        return transformedData

    def _transformCsvRow(self,csvRow) :
        date = csvRow.ORDERDATE
        if(isinstance(date,str)):
            date = utility.strToDate(date)
        date = datetime.date(date.year,date.month,date.day)
        
        quantity = csvRow.QUANTITYORDERED
        sales = csvRow.SALES
        status = utility.statusToCode(csvRow.STATUS)
        product_code = csvRow.PRODUCTCODE
        state = csvRow.STATE
        country = csvRow.COUNTRY
        postal_code = csvRow.POSTALCODE

        return sales_model.Sale(quantity,postal_code,sales,date,status,
    state,country,product_code)
