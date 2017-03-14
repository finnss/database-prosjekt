import mysql.connector
from mysql.connector import errorcode


"""Hei finn!"""

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'test_schema',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


#####
# Each use case is in it's own comment block, seperated by their titles.
# Copy the relevant block to your file and uncomment to use.
# The examples assume a table 'Users' with columns 'id', 'age', 'first', 'last'.
#####


# Create database
"""
DB_NAME = 'test_schema'

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {%s} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {%s}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
"""


# Add tables
"""
TABLES = {}
TABLES['treningsøkt'] = (
    "CREATE TABLE `treningsøkt` ("
    "  `øktId` int(11) NOT NULL AUTO_INCREMENT,"
    "  `varighet` int(10) NOT NULL,"
    "  `Idrett` varchar(14) NOT NULL,"
    " PRIMARY KEY (`øktId`)"
    ") ENGINE=InnoDB")


for name, ddl in TABLES.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
"""


# Insert data
"""
add_user = ("INSERT INTO Users "
               "(id, age, first, last) "
               "VALUES (%s, %s, %s, %s)")

sim1haha = ("2", "22", "Simen", "Haga")

cursor.execute(add_user, sim1haha)
"""


# Select data
"""
query = ("SELECT * FROM Users")

cursor.execute(query)

for (id, age, first, last) in cursor:
  print("{:s} {:s} is {:d} years old and has id {:d}.".format(
    first, last, age, id))

"""

cnx.commit()
cursor.close()
cnx.close()