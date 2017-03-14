import mysql.connector
from mysql.connector import errorcode
import time
import datetime


config = {
  'user': 'root',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'test_schema',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

hent_varighet = ("SELECT øktid FROM utført"
                " WHERE økt_dato BETWEEN %s AND %s")

hent_økter = ("SELECT FROM "
              "WHERE økt_dato BETWEEN %s AND %s")

hent_øvelser = ("SELECT øvelse_navn FROM øvelse"
                " WHERE økt_dato BETWEEN %s AND %s")

økt_dato_slutt = datetime.datetime.now().strftime("%Y, %m, %d")
DD = datetime.timedelta(days=30)
økt_dato_starter = økt_dato_slutt - DD
økt_dato_start = økt_dato_starter.strftime("%Y, %m, %d")

cursor.execute(hent_varighet, (økt_dato_start, økt_dato_slutt))


"""
    koble til database
        koble til

    hent data
        where dato ikke  er eldre enn en måned
            hent antall øvelser
            hent antall økter
            hent varighet for økter
                summer varighet

    koble fra database?

    returner data"""

