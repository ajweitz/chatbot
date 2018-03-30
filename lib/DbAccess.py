from lib import Configurator
import psycopg2

class DbAccess:

    DB_CONFIG = "database.ini"

    GREETINGS_TABLE = "greetings"
    GREETINGS_COLUMNS = {"name":"gname","rating":"rating"}
    UNKNOWN_TABLE = "unknown"
    UNKNOWN_COLUMNS = {"name":"uname","rating":"rating"}

    TABLE_UNKNOWN = ""

    def __init__(self):
        self.config = Configurator.Configurator()
        self.dbConfig = self.config.dbConfig(self.DB_CONFIG)
        #connecting to DB
        self.conn = psycopg2.connect(host=self.dbConfig["host"],database=self.dbConfig["database"], user=self.dbConfig["user"], password=self.dbConfig["password"])

    def getGreetings(self, precision):
        t = self.GREETINGS_TABLE
        c = self.GREETINGS_COLUMNS
        return self.getTopAnswers(precision, t, c['name'], c['rating'])

    def getUnknowns(self, precision):
        t = self.UNKNOWN_TABLE
        c = self.UNKNOWN_COLUMNS
        return self.getTopAnswers(precision, t, c['name'], c['rating'])

    # method for the most common way to fetch data
    def getTopAnswers(self, precision, table, cname, crating):
        cur = self.conn.cursor()
        query = "SELECT {} FROM {} ORDER BY {} LIMIT {}".format(cname, table, crating, precision)
        cur.execute(query)
        result = tuplesToArr(cur.fetchall())
        cur.close()
        return result

# Helper functions
def tuplesToArr(tuples):
    result = []
    for tuple in tuples:
        result.append(list(tuple)[0])
    return result
