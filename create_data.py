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
    "(varighet,idrett)"
    "VALUES (%s, %s)"
)

add_utført = (
    "INSERT INTO utført"
    "(repetisjoner,sett,vekt,lengde,kommentar,øktid,øvelse_navn)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s)"
)

add_øvelse = (
    "INSERT INTO øvelse"
    "(øvelse_navn,beskrivelse)"
    "VALUES (%s,%s)"
)

add_utendørsøkt = (
    "INSERT INTO utendørsøkt "
    "(øktid, ventilasjon,antall_tilskuere) "
    "VALUES (%s, %s, %s)"
)

add_innendørsøkt = (
    "INSERT INTO innendørsøkt "
    "(øktid, ventilasjon,antall_tilskuere) "
    "VALUES (%s, %s, %s)"
)

add_mål = (
    "INSERT INTO mål"
    "(målid, tidsfrist, repetisjoner, sett, vekt, lengde, kommentar, brukernavn, øvelse_navn)"
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
)


simen = ("sim1haha","mann","22")
økt = ("01:00:00","vektløfting")
def simen_har_trent_økt(øktId):
    return (simen[0],øktId,"2017-01-1",økt[0],"meh","meh")
øvelse = ("Markløft","Standard markløft")
def simen_har_utført(øktId):
    return ("10","3","120",None,"gikk bra",øktId,øvelse[0])
simen_har_mål = ("10", "2017-01-1", "10", "4", "125", None, "lol moro", simen[0], "Markløft")



def execute_create_data(cursor):
    cursor.execute(add_user, simen)
    cursor.execute(add_øvelse,øvelse)
    cursor.execute(add_treningsøkt,økt)
    øktId = cursor.lastrowid
    cursor.execute(add_utført,simen_har_utført(øktId))
    cursor.execute(add_har_trent,simen_har_trent_økt(øktId))
    cursor.execute(add_mål, simen_har_mål)
    print('Data lagt til OK')

