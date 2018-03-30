from lib import Configurator
import psycopg2

class DbAccess:

    DB_CONFIG = "database.ini"

    def __init__(self):
        self.config = Configurator.Configurator()
        self.dbConfig = self.config.dbConfig(self.DB_CONFIG)
        #connecting to DB
        self.conn = psycopg2.connect(host=self.dbConfig["host"],database=self.dbConfig["database"], user=self.dbConfig["user"], password=self.dbConfig["password"])
