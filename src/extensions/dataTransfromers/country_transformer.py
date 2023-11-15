from ast import List
import csv

from models.sales_model import Sale



class CountryTransformer :
    countries = {}

    def __init__(self,countriesSource):
        with open(countriesSource, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.countries[row['Name']] = row['Code']

    def transformData(self,rawData):
        transformedData = []
        for row in rawData :
            row.country = self.countries[row.country]
            transformedData.append(row)
        return transformedData            