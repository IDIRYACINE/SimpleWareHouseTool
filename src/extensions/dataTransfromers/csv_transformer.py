import data_transformer
from models.sales_model import sales_model

class CsvTransformer(data_transformer.DataTransformer): 

    def transformData(self,rawData):
        transformedData = []

        for row in rawData.iterrows():
            transformedData.append(self._transformCsvRow(row))
        
        return transformedData

    def _transformCsvRow(csvRow) :
        quantity = csvRow[0]
        unit_price = csvRow[1]
        sales = csvRow[2]
        date = csvRow[3]
        status = csvRow[4]
        product_code = csvRow[5]
        customer_name = csvRow[6]
        phone = csvRow[7]
        city = csvRow[8]
        state = csvRow[9]
        country = csvRow[10]
        postal_code = csvRow[11]

        return sales_model.Sale(quantity,unit_price,postal_code,sales,date,status,phone,city,
    state,country,customer_name,product_code)