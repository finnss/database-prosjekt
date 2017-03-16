import mysql.connector

def executeQueries():
    dateQueryStyrke = (
    " SELECT t.idrett,h.dato, ø.øvelse_navn"
    " FROM   bruker b, har_trent h, treningsøkt t, utført u,øvelse ø"
    " WHERE h.brukernavn = b.brukernavn "
    " AND h.øktid = t.øktid"
    " AND u.øktid = t.øktid"
    " AND u.øvelse_navn = ø.øvelse_navn"
    )

    return dateQueryStyrke


def print_øvelser(cursor):
    cursor.execute(executeQueries())

    print("\nFølegnde treninger og øvelser er kjent:\n"
          "+--------------------+--------------------+--------------------+\n"
          "|       Dato         |       Idrett       |       Øvelse       +\n"
          "+--------------------+--------------------+--------------------+")
    for (idrett,dato,øvelse_navn) in cursor:
        print("|{:20s}|{:20s}|{:20s}|".format(dato.strftime('%d/%m/%Y'),idrett, øvelse_navn))

    print("+--------------------+--------------------+--------------------+\n")
