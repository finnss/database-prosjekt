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

add_har_trent = ("INSERT INTO har_trent"
                 "(brukernavn,øktid,dato,Tidspunkt,prestasjon,personlig_form)"
                 "VALUES (%s,%s,%s,%s,%s,%s)")

add_treningsøkt = ("INSERT INTO treningsøkt "
            "(øktid,brukerid,tidspunkt,idrett)"
            "VALUES (%s, %s, %s, %s)")

simen = ("Simen Haga","mann","22")
økt = ("1",simen[0],"2017-03-15","vektløfting")


cursor.execute(add_user, simen)


cnx.commit()
cursor.close()
cnx.close()