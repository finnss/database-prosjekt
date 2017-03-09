import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'test_schema',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Add tables

"""
DB_NAME = 'Test_schema'
TABLES = {}
TABLES['Test_schema'] = (
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

query = ("SELECT * FROM Users")

cursor.execute(query)

for (id, age, first, last) in cursor:
  print("{:s} {:s} is {:d} years old and has id {:d}.".format(
    first, last, age, id))

cnx.commit()

cursor.close()
cnx.close()