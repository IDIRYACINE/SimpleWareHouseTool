
from extensions.dataExtractors.data_extractor import Extractor
from core import utility
from core import data_reader
from core.sql_server import SqlServer
from models.special_values import RawSaleColumnNames

dataSourcesDirectory = utility.getSampleDataDirectory()


importedColumns = [
    RawSaleColumnNames.PRICEEACH, 
    RawSaleColumnNames.QUANTITYORDERED,
    RawSaleColumnNames.SALES,
    RawSaleColumnNames.ORDERDATE,
    RawSaleColumnNames.STATUS,
    RawSaleColumnNames.PRODUCTCODE,
    RawSaleColumnNames.CITY,
    RawSaleColumnNames.STATE, 
    RawSaleColumnNames.COUNTRY,
    RawSaleColumnNames.POSTALCODE
    ]

dataFile = dataSourcesDirectory + "/sales_data.xlsx"
dataExctractor : Extractor = data_reader.get_exctractor(dataFile,importedColumns)
dataExctractor.open_data_source(dataFile)
transformedData = dataExctractor.extract_data('IDIr',2, 10)

configFilePath = utility.getRootDirectory() + "/config.ini"
configs = utility.loadIniFile(configFilePath)

databaseAuth = utility.authObjectFromConfig(configs)
myDatabase = SqlServer()
myDatabase.connect(databaseAuth)

myDatabase.executeInsertQuery(transformedData)
