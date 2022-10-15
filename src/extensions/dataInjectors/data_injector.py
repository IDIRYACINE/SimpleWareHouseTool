from abc import ABC, abstractmethod


class DatabaseInjector(ABC) :

    @abstractmethod
    def inject_data(self, data) :
        """Inject the data into the database"""
        pass

    @abstractmethod
    def open_database(self , databaseAuthObject) :
        """Open the database"""
        pass

    @abstractmethod
    def close_database(self) :
        """Close the database"""
        pass

    @abstractmethod
    def save_injection_progress(self) :
        """Save the injection progress"""
        pass

    @abstractmethod
    def load_injection_progress(self) :
        """Load the injection progress"""
        pass
    
    @abstractmethod
    def resume_injection(self) :
        """Resume the injection"""
        pass


class DatabaseAuthObject : 
    """Database authentication object"""
    _username = None
    _password = None
    _host = None
    _port = None
    _database = None

    def __init__(self, username, password, host, port, database) :
        self._username = username
        self._password = password
        self._host = host
        self._port = port
        self._database = database

    def get_username(self) :
        return self._username

    def get_password(self) :
        return self._password

    def get_host(self) :
        return self._host

    def get_port(self) :
        return self._port

    def get_database(self) :
        return self._database                                