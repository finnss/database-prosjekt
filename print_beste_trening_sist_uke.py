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



query = (
" SELECT b.brukernavn, b.kjønn, b.alder FROM bruker b,har_trent h, treningsøkt t,"
" innendørsøkt inn, utendørsøkt ut, utført u,øvelse ø,mål m"
" WHERE b.brukernavn = h.brukernavn"
" AND h.øktid = t.øktid")



cursor.execute(query)

for (brukernavn,kjønn,alder) in cursor:
  print("{:s} er {:d} år og {:s}.".format(
    brukernavn,alder,kjønn))


cnx.commit()
cursor.close()
cnx.close()