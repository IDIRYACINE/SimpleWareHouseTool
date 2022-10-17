from abc import ABC, abstractmethod
import pymssql 


class DatabaseAuthObject : 
    """Database authentication object"""
    _username = None
    _password = None
    _host = None
    _port = None
    _database = None

    def __init__(self, username : str, password :str, host:str ,port:str,  database:str) :
        self._username = username
        self._password = password
        self._host = host
        self._database = database
        self._port = port

    def get_username(self) :
        return self._username

    def get_password(self) :
        return self._password

    def get_host(self) :
        return self._host

    def get_database(self) :
        return self._database

    def get_port(self) :
        return self._port    

class ISqlServer(ABC) :

    @abstractmethod
    def connect(self, databaseAuthObject : DatabaseAuthObject) :
        """Connect to the database"""
        pass

    @abstractmethod
    def disconnect(self) :
        """Disconnect from the database"""
        pass

    @abstractmethod
    def executeInsertQuery(self, query) :
        """Execute the query"""
        pass

    @abstractmethod
    def executeSelectQuery(self, query) :
        """Execute the query"""
        pass


class SqlServer(ISqlServer) :
    _conn = None

    def connect(self, databaseAuthObject) :
        self._conn =  pymssql.connect(
            server = databaseAuthObject.get_host(), 
            user = databaseAuthObject.get_username(), 
            password = databaseAuthObject.get_password(),
            database = databaseAuthObject.get_database())

    def disconnect(self) :
        self._conn.close()

    def executeInsertQuery(self, query) :
        cursor = self._conn.cursor()
        cursor.execute(query)
        self._conn.commit()

    def executeSelectQuery(self, query) :
        cursor = self._conn.cursor()
        cursor.execute(query)
        
        result = []
        for row in cursor :
            result.append(row)

        return result    


