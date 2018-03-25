import configparser
import os
import psycopg2
from subprocess import call

DB_NAME = "chatbot"
DB_SCRIPT = "install.sql"
DB_CONFIG = "database.ini"
DEFAULT_GREETINGS_FILE = "greetings.lsv"
DEFAULT_UNKNOWN_FILE = "unknown.lsv"
DEFAULT_GREETINGS_TABLE = "greetings"
DEFAULT_UNKNOWN_TABLE = "unknown"
INSTALL_FOLDER = "install"
DEFAULTS_FOLDER = "defaults"
HOST = 'localhost'

#ini file config
SECTION = "postgresql"
HOST_KEY = 'host'
USER_KEY = 'user'
PASS_KEY = 'password'
DB_KEY = 'database'

def insert(file, table, col, conn):
    sql = "INSERT INTO "+table+"("+col+") VALUES(%s)"
    cur = conn.cursor()
    with open(os.path.join(DEFAULTS_FOLDER, file)) as fp:
        line = fp.readline()
        while line:
            cur.execute(sql, (line.rstrip(),))
            line = fp.readline()
        conn.commit()
        cur.close()
    return

username = input("Enter postgresql username:\n")
password = input("Enter postgresql password:\n")

# TODO: add option to specify a port
# TODO: handle error in case we didn't find createdb or psql

# Create DB and Tables
os.environ["PGPASSWORD"] = password
os.system("createdb --username {} {}".format(username, DB_NAME))
os.system("psql --username {} -ef {} {}".format(username, os.path.join(INSTALL_FOLDER, DB_SCRIPT), DB_NAME))


# create a config file
config = configparser.ConfigParser()
config.add_section(SECTION)
config[SECTION][HOST_KEY] = HOST
config[SECTION][DB_KEY] = DB_NAME
config[SECTION][USER_KEY] = username
config[SECTION][PASS_KEY] = password

#save to file
with open(DB_CONFIG, 'w') as configfile:
    config.write(configfile)

# Connect to DB
conn = psycopg2.connect("dbname={} user={} password={}".format(DB_NAME,username,password))
#fill with data
insert(DEFAULT_GREETINGS_FILE, DEFAULT_GREETINGS_TABLE, "gname", conn)
insert(DEFAULT_UNKNOWN_FILE, DEFAULT_UNKNOWN_TABLE, "uname", conn)
#close connection
conn.close()


