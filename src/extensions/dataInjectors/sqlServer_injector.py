import data_injector

class MySqlServerInjector(data_injector.DatabaseInjector) :

    databaseObject = None
 
    def inject_data(self, data) :
        """Inject the data into the database"""
        pass

    def open_database(self , databaseAuthObject) :
        """Open the database"""
        pass

    def close_database(self) :
        """Close the database"""
        pass

    def save_injection_progress(self) :
        """Save the injection progress"""
        pass

    def load_injection_progress(self) :
        """Load the injection progress"""
        pass
    
    def resume_injection(self) :
        """Resume the injection"""
        pass