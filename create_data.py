import mysql.connector

add_user = (
    " INSERT INTO bruker "
    " (brukernavn,kjønn,alder) "
    " VALUES (%s, %s, %s)"
)

add_har_trent = (
    "INSERT INTO har_trent"
    "(brukernavn,øktid,dato,Tidspunkt,prestasjon,personlig_form)"
    "VALUES (%s,%s,%s,%s,%s,%s)"
)

add_treningsøkt = (
    "INSERT INTO treningsøkt "
    "(øktid,varighet,idrett)"
    "VALUES (%s, %s, %s)"
)


add_utført = (
    "INSERT INTO utført"
    "(repetisjoner,sett,vekt,lengde,kommentar,øktid,øvelse_navn)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s)"
)

add_øvelse = (
    "INSERT INTO øvelse"
    "(øvelse_navn,beskrivelse,antall_reps,antall_sett,belastning)"
    "VALUES (%s,%s,%s,%s,%s)"
)


simen = ("Simen Haga","mann","22")
økt = ("1","01:00:00","vektløfting")
simen_har_trent_økt = (simen[0],økt[0],"2017-01-1",økt[1],"meh","meh")
øvelse = ("Markløft","Standard markløft",None,None,None)
simen_har_utført = ("10","3","120",None,"gikk bra",økt[0],øvelse[0])


def execute_create_data(cursor, cnx):
    cursor.execute(add_user, simen)
    cursor.execute(add_treningsøkt,økt)
    cursor.execute(add_har_trent,simen_har_trent_økt)
    cursor.execute(add_øvelse,øvelse)
    cursor.execute(add_utført,simen_har_utført)

    cnx.commit()