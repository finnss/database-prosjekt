import mysql.connector
from mysql.connector import errorcode
import time
import datetime

def createMål(cursor):
    add_mål = (
        "INSERT INTO mål"
        "(målid, tidsfrist, repetisjoner, sett, vekt, lengde, kommentar, brukernavn, øvelse_navn)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
    
    cursor.execute(add_mål, mål)