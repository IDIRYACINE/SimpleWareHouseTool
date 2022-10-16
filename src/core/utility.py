import os,time

def getSampleDataDirectory():
    os.chdir("../sampleData")
    return os.getcwd()

def getCurrentTimestamp():
    return time.time()

def dateToTimestamp(date) :
    return time.mktime(date.timetuple())

def timestampToDate(timestamp) :
    return time.strftime('%Y-%m-%d-%h-%min', time.localtime(timestamp))

def loadIniFile(filename):
    import configparser
    config = configparser.ConfigParser()
    config.read(filename)
    return config    