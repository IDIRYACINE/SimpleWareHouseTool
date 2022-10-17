import time
import extensions.dataTransfromers.data_transformer as data_transformer
from core import utility
import pandas as pd
from models import sales_model

class CsvTransformer(data_transformer.DataTransformer): 

    def transformData(self,rawData : pd.DataFrame):
        transformedData = []
        print(rawData.head())
        for row in rawData.itertuples():
            tRow = self._transformCsvRow(row)
            transformedData.append(tRow)
        return transformedData

    def _transformCsvRow(self,csvRow) :
        date = utility.strToDate(csvRow.ORDERDATE)
        date = utility.dateToTimestamp(date)

        quantity = csvRow.QUANTITYORDERED
        sales = csvRow.SALES
        status = utility.statusToCode(csvRow.STATUS)
        product_code = csvRow.PRODUCTCODE
        state = csvRow.STATE
        country = csvRow.COUNTRY
        postal_code = csvRow.POSTALCODE

        return sales_model.Sale(quantity,postal_code,sales,date,status,
    state,country,product_code)
