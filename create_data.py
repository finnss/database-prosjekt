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

add_user = ("INSERT INTO bruker "
            "(brukernavn,kjønn,alder) "
            "VALUES (%s, %s, %s)")

simen = ("Simen Haga","mann","22")


cursor.execute(add_user, simen)


cnx.commit()
cursor.close()
cnx.close()