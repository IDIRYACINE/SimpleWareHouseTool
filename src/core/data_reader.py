from models.sales_model import Sale
from extensions.dataExtractors import excel_exctractor
from extensions.dataExtractors import csv_extractor
from extensions.dataExtractors import data_extractor
import pathlib

def get_exctractor(filename: str , importedColumns:list) -> data_extractor.Extractor :
    ext = pathlib.Path(filename).suffix
    
    dataExctractor = None

    if (ext == ".xlsx"):
        dataExctractor = excel_exctractor.ExcelExtractor(importedColumns)

    if (ext == ".csv"):
        dataExctractor = csv_extractor.CsvExctractor(importedColumns)

    return dataExctractor
