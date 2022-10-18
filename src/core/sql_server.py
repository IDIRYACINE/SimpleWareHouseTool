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
        cursor.execute("SELECT * FROM sales")

        result = []
        for row in cursor:
            result.append(row)

        return result

    def _salesListToInsertQuery(self, sales: list[sales_model.Sale]) -> str:
        query = "INSERT INTO sales (quantity, postal_code, sales, date, status, city, country,product_code) VALUES "
        for sale in sales:
            query += "({0}, '{1}', '{2}', '{3}', {4}, '{5}', {6},{7}),".format(
                sale.quantity,
                sale.postal_code,
                sale.sales,
                sale.date,
                sale.status,
                sale.state,
                sale.country,
                sale.product_code
            )
            print(query)
        return query[:-1]


