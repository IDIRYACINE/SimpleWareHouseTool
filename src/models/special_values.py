from enum import Enum

OrderStatusDictionary = {
    "In Process": 0,
    "On Hold": 1,
    "Shipped" : 2,
    "Cancelled" : 3,
}


class RawSaleColumnNames(Enum) :
    ORDERNUMBER = "ORDERNUMBER"
    QUANTITYORDERED = "QUANTITYORDERED"
    PRICEEACH = "PRICEEACH"
    ORDERLINENUMBER = "ORDERLINENUMBER"
    SALES = "SALES"
    ORDERDATE = "ORDERDATE"
    STATUS = "STATUS"
    QTR_ID = "QTR_ID"
    MONTH_ID = "MONTH_ID"
    YEAR_ID = "YEAR_ID"
    PRODUCTLINE = "PRODUCTLINE"
    MSRP = "MSRP"
    PRODUCTCODE = "PRODUCTCODE"
    CUSTOMERNAME = "CUSTOMERNAME"
    PHONE = "PHONE"
    ADDRESSLINE1 = "ADDRESSLINE1"
    ADDRESSLINE2 = "ADDRESSLINE2"
    CITY = "CITY"
    STATE = "STATE"
    POSTALCODE = "POSTALCODE"
    COUNTRY = "COUNTRY"
    TERRITORY = "TERRITORY"
    CONTACTLASTNAME = "CONTACTLASTNAME"
    CONTACTFIRSTNAME = "CONTACTFIRSTNAME"
    DEALSIZE = "DEALSIZE"

ExcelDataColumnsDict = {
    RawSaleColumnNames.ORDERNUMBER : "A",
    RawSaleColumnNames.QUANTITYORDERED : "B",
    RawSaleColumnNames.PRICEEACH : "C",
    RawSaleColumnNames.ORDERLINENUMBER : "D",
    RawSaleColumnNames.SALES : "E",
    RawSaleColumnNames.ORDERDATE : "F",
    RawSaleColumnNames.STATUS : "G",
    RawSaleColumnNames.QTR_ID : "H",
    RawSaleColumnNames.MONTH_ID : "I",
    RawSaleColumnNames.YEAR_ID : "J",
    RawSaleColumnNames.PRODUCTLINE : "K",
    RawSaleColumnNames.MSRP : "L",
    RawSaleColumnNames.PRODUCTCODE : "M",
    RawSaleColumnNames.CUSTOMERNAME : "N",
    RawSaleColumnNames.PHONE : "O",
    RawSaleColumnNames.ADDRESSLINE1 : "P",
    RawSaleColumnNames.ADDRESSLINE2 : "Q",
    RawSaleColumnNames.CITY : "R",
    RawSaleColumnNames.STATE : "S",
    RawSaleColumnNames.POSTALCODE : "T",
    RawSaleColumnNames.COUNTRY : "U",
    RawSaleColumnNames.TERRITORY : "V",
    RawSaleColumnNames.CONTACTLASTNAME : "W",
    RawSaleColumnNames.CONTACTFIRSTNAME : "X",
    RawSaleColumnNames.DEALSIZE : "Y"
   
}

