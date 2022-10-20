from extensions.dataExtractors import csv_exctractor as extractor
from extensions.dataTransfromers import csv_transformer as transformer
from core import utility
from core.sql_server import SqlServer
from models.special_values import RawSaleColumnNames

dataSourcesDirectory = utility.getSampleDataDirectory()

importedColumns = [RawSaleColumnNames.PRICEEACH, RawSaleColumnNames.QUANTITYORDERED, RawSaleColumnNames.SALES,
    RawSaleColumnNames.ORDERDATE, RawSaleColumnNames.STATUS, RawSaleColumnNames.PRODUCTCODE,
    RawSaleColumnNames.CITY, RawSaleColumnNames.STATE, RawSaleColumnNames.COUNTRY,
     RawSaleColumnNames.POSTALCODE]

csvExctractor = extractor.CsvExtractor(importedColumns)
csvExctractor.open_data_source(dataSourcesDirectory + "/sales_data_sample.csv")
transformedData = csvExctractor.extract_data(0, 10)

configFilePath = utility.getRootDirectory() + "/config.ini"
configs = utility.loadIniFile(configFilePath)

databaseAuth = utility.authObjectFromConfig(configs)
myDatabase = SqlServer()
myDatabase.connect(databaseAuth)

myDatabase.executeInsertQuery(transformedData)
