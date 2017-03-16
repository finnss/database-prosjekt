import mysql.connector
from mysql.connector import errorcode
import time
import datetime


def getMål(cursor):

    hent_mål = ("SELECT målid, tidsfrist, repetisjoner, sett, vekt, lengde, kommentar, brukernavn, øvelse_navn FROM mål")

    cursor.execute(hent_mål)

    alle_maal = ""

    for ( målid, tidsfrist, repetisjoner, sett, vekt, lengde, kommentar, brukernavn, øvelse_navn) in cursor:
        alle_maal += ("Mål med id: {}, tillhørte bruker: {}.\nØvelse: {}\nrepetisjoner: {}\nSet: {}\nVekt {}\nLengde {}\nTidsfrist {}\n Tilhørende kommentar: {} \n" ).format(
        målid, brukernavn, øvelse_navn, repetisjoner, sett, vekt, lengde, tidsfrist, kommentar)

    print (alle_maal)




