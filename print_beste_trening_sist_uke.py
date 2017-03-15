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



dateQueryStyrke = (
" SELECT h.dato, h.tidspunkt FROM bruker b,har_trent h, treningsøkt t,"
" utført u,øvelse ø"
" WHERE b.brukernavn = h.brukernavn"
" AND h.øktid = t.øktid"
" AND u.øktid = t.øktid"
" AND u.øvelse_navn = ø.øvelse_navn"
)

dateQueryKondis = (
" SELECT h.dato, h.tidspunkt FROM bruker b,har_trent h, treningsøkt t,"
" utført u,øvelse ø"
" WHERE b.brukernavn = h.brukernavn"
" AND h.øktid = t.øktid"
" AND u.øktid = t.øktid"
" AND u.øvelse_navn = ø.øvelse_navn"
""
)


bestStyrkeQuery = (
" SELECT b.brukernavn, b.kjønn, b.alder FROM bruker b,har_trent h, treningsøkt t,"
" utført u,øvelse ø"
" WHERE b.brukernavn = h.brukernavn"
" AND h.øktid = t.øktid"
" AND u.øktid = t.øktid"
" AND u.øvelse_navn = ø.øvelse_navn"
)


bestKondisQuery = (
" SELECT b.brukernavn, b.kjønn, b.alder FROM bruker b,har_trent h, treningsøkt t,"
" utført u,øvelse ø"
" WHERE b.brukernavn = h.brukernavn"
" AND h.øktid = t.øktid"
" AND u.øktid = t.øktid"
" AND u.øvelse_navn = ø.øvelse_navn"
)


cursor.execute(dateQueryStyrke)

for (dato,tidspunkt) in cursor:
  print("Beste styrketrening var på den {:s} klokken {:s}.".format(
    dato,tidspunkt))


cnx.commit()
cursor.close()
cnx.close()