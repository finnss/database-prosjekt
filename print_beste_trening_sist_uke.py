import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'test_schema',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()



query = ("SELECT * FROM bruker")

cursor.execute(query)

for (brukernavn,kjønn,alder) in cursor:
  print("{:s} er {:d} år og {:s}.".format(
    brukernavn,alder,kjønn))




cnx.commit()
cursor.close()
cnx.close()