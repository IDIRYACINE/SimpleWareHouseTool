from abc import ABC, abstractmethod
import pymysql
from models import sales_model


class DatabaseAuthObject:
    """Database authentication object"""
    _username = None
    _password = None
    _host = None
    _port = None
    _database = None

    def __init__(self, username: str, password: str, host: str, port: str,  database: str):
        self._username = username
        self._password = password
        self._host = host
        self._database = database
        self._port = port

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_host(self):
        return self._host

    def get_database(self):
        return self._database

    def get_port(self):
        return self._port


class ISqlServer(ABC):

    @abstractmethod
    def connect(self, databaseAuthObject: DatabaseAuthObject):
        """Connect to the database"""
        pass

    @abstractmethod
    def disconnect(self):
        """Disconnect from the database"""
        pass

    @abstractmethod
    def executeInsertQuery(self, data):
        """Execute the query"""
        pass

    @abstractmethod
    def executeSelectQuery(self):
        """Execute the query"""
        pass


class SqlServer(ISqlServer):
    _conn = None

    def connect(self, databaseAuthObject):
        self._conn = pymysql.connect(
            host=databaseAuthObject.get_host(),
            user=databaseAuthObject.get_username(),
            password=databaseAuthObject.get_password(),
            unix_socket="/run/mysqld/mysqld.sock",
            database=databaseAuthObject.get_database())

    def disconnect(self):
        self._conn.close()

    def executeInsertQuery(self, data):
        cursor = self._conn.cursor()
        query = self._salesListToInsertQuery(data)
        cursor.execute(query)
        self._conn.commit()

    def executeSelectQuery(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT * FROM Sales")

        result = []
        for row in cursor:
            result.append(row)

        return result

    def _salesListToInsertQuery(self, sales: list[sales_model.Sale]) -> str:
        query = "INSERT INTO Sales (sale_quantity, postal_code, sale_profit, sale_date, sale_status, country,product_code) VALUES "
        
        saleIndex = 0

        for sale in sales:
            postal_code = 51247.0
            if(sale.postal_code != '') :
                postal_code = sale.postal_code

            query += "({0}, '{1}', '{2}', '{3}', '{4}', '{5}','{6}')".format(
                sale.quantity,
                postal_code,
                sale.sales,
                sale.date,
                sale.status,
                sale.country,
                sale.product_code
            )
            if(saleIndex != len(sales) - 1):
                query = query + ","
            saleIndex = saleIndex + 1
        query = query + ";"    
        print(query)
        return query[:-1]


