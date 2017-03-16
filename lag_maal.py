import mysql.connector
import time
import datetime

def createMål(cursor):
    add_mål = (
        "INSERT INTO mål"
        "(målid, tidsfrist, repetisjoner, sett, vekt, lengde, kommentar, brukernavn, øvelse_navn)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

    print("Fyll inn data. skriv None om data ikke finnes for punkt")

    id= input("Mål-ID: ")
    date_entry = input('Tidsfrist på YYYY-MM-D format: ')
    year, month, day = map(int, date_entry.split('-'))
    tid = datetime.date(year, month, day)
    rep = input("Repetisjoner: ")
    sett=input("Set: ")
    Weight = input("Vekt: ")
    Length = input("lengde: ")
    comment = input("kommentar: ")
    username = input("Brukernavn: ")
    name= input("Navn på Øvelse: ")
    mål =(id, tid, rep, sett, Weight, Length, comment, username,name)

    cursor.execute(add_mål, mål)
    print("Mål Lagt til.\n")