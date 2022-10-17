from configparser import ConfigParser
import os,datetime
from models import special_values
from core.sqlServer import DatabaseAuthObject

def getSampleDataDirectory():
    os.chdir("../sampleData")
    return os.getcwd()

def getRootDirectory():
    os.chdir("..")
    return os.getcwd()

def getCurrentTimestamp():
    return datetime.time()

def dateToTimestamp(date) :
    return datetime.datetime.timestamp(date)

def strToDate(dateStr) :
    return datetime.datetime.strptime(dateStr, '%m/%d/%Y %H:%M')

def timestampToDate(timestamp) :
    return datetime.localtime(timestamp)

def loadIniFile(filename):
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    return config    

def statusToCode(status) :
    return special_values.OrderStatusDictionary[status]
   
def authObjectFromConfig(configs : ConfigParser) -> DatabaseAuthObject :  
    databaseConfigSection = configs['DatabaseConfigs']

    return DatabaseAuthObject(
        databaseConfigSection['username'],
        databaseConfigSection['password'],
        databaseConfigSection['host'] ,
        databaseConfigSection['port'],
        databaseConfigSection['database']
    )