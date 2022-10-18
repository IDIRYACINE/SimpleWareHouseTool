from extensions.dataExtractors import csv_exctractor as extractor
from extensions.dataTransfromers import csv_transformer as transformer
from core import utility
from core.sql_server import SqlServer

dataSourcesDirectory = utility.getSampleDataDirectory()

importedColumns = ['PRICEEACH', 'QUANTITYORDERED', 'SALES', 'ORDERDATE', 'STATUS', 'PRODUCTCODE',
                   'CUSTOMERNAME', 'PHONE', 'CITY', 'STATE', 'COUNTRY', 'POSTALCODE']

csvExctractor = extractor.CsvExtractor(importedColumns)
csvExctractor.open_data_source(dataSourcesDirectory + "/sales_data_sample.csv")
extractedData = csvExctractor.extract_data(0, 10)


csvTransformer = transformer.CsvTransformer()

transformedData = csvTransformer.transformData(extractedData)

configFilePath = utility.getRootDirectory() + "/config.ini"
configs = utility.loadIniFile(configFilePath)

databaseAuth = utility.authObjectFromConfig(configs)
myDatabase = SqlServer()
myDatabase.connect(databaseAuth)

myDatabase.executeInsertQuery(transformedData)
