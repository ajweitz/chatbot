import pip

def install(package):
    pip.main(['install', package])


install('psycopg2')