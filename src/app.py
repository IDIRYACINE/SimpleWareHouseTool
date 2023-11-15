from extensions.dataExtractors.data_extractor import Extractor
from core import utility
from core import data_reader
from core.sql_server import SqlServer
from extensions.dataTransfromers.country_transformer import CountryTransformer
from models.special_values import RawSaleColumnNames

# Configs Initialization
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

configs = utility.loadIniFile()
dataSourcesDirectory = utility.getSampleDataDirectory()
sessionConfigs = configs["Session"]
dataFile = dataSourcesDirectory + "/" + sessionConfigs["dataSource"]
# Exctract  And Process Data
dataExctractor : Extractor = data_reader.get_exctractor(dataFile,importedColumns)
dataExctractor.open_data_source(dataFile)


transformedData = dataExctractor.extract_data(
    sessionConfigs["dataSheet"],
    int(sessionConfigs["startRow"]), 
    int(sessionConfigs["endRow"])
    )

countryTransformer = CountryTransformer(dataSourcesDirectory + "/" + sessionConfigs["countriesSource"])
transformedData = countryTransformer.transformData(transformedData)    


# Connect to the database
databaseAuth = utility.authObjectFromConfig(configs)
myDatabase = SqlServer()
myDatabase.connect(databaseAuth)

# Insert data into the database
myDatabase.executeInsertQuery(transformedData)
