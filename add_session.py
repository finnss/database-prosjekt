import sys
import mysql.connector
from create_data import *

def create_session(cursor, bruker):
    øktid = cursor.lastrowid
    date = input("Skriv inn dato(YYYY-MM-DD): ")
    time = input("Skriv inn tidspunkt(HH:MM:SS): ")
    env = input("Var økten innendørs eller utendørs (i/u)?: ")
    sport = input("Hva slags idrett?: ")
    duration = input("Øktens varighet(HH:MM:SS): ")
    form = input ("Hvordan var dagens form: ")
    prestasjon = input("Bemerkelsesverdige prestasjoner: ")
    # insert data into treningsøkt
    data_treningsøkt = (øktid, duration, sport)
    cursor.execute(add_treningsøkt, data_treningsøkt)
    if(env=="i"):
        ventilation = input("Hvordan var ventilasjonen: ")
        spectaters= input("Antall tilskuere: ")
        data_innendørsøkt = (øktid,ventilation, spectaters)
        cursor.execute(add_innendørsøkt, data_innendørsøkt)
    elif(env=="u"):
        temp = input("Temperatur: ")
        weather = input("Vær: ")
        data_utendørsøkt = (øktid, temp, weather)
        cursor.execute(add_utendørsøkt, data_utendørsøkt)

    #hartrent relation
    data_hartrent = (bruker, øktid, date, time, form, prestasjon)
    cursor.execute(add_har_trent,data_hartrent)
    #loop to add new exercises
    fortsett = 'j'
    while(fortsett=='j'):
        create_exercise(cursor)
        input(("fortsett(j/n):").lower())

def create_exercise(cursor):
    # Info regarding exercise (øvelse)
    name = input("Navn på øvelse: ")
    desc = input("Beskrivelse av øvelsen: ")
    type = input(("Kondisjonsøvelse eller styrkeøvelse (k/s): ").lower())
    if(type=="k"):
        sett = input("Antall sett: ")
        repetisjoner = input("Antall repetisjoner: ")
        lengde = input("Distance: ")
        kommentar = input("Kommentar: ")
        data_kondisjonsøvelse = (name, desc)
        data_utført = (repetisjoner,sett,lengde,kommentar)
        cursor.execute(add_øvelse, data_kondisjonsøvelse)
        cursor.execute(add_utført, data_utført)
    elif(type=="s"):
        sett = input("Antall sett: ")
        repetisjoner = input("Antall repetisjoner: ")
        vekt = input("Vekt: ")
        kommentar = input("Kommentar: ")
        data_styrkeøvelse = (name, desc)
        data_utført = (repetisjoner, sett, vekt,kommentar)
        cursor.execute(add_øvelse, data_styrkeøvelse)
        cursor.execute(add_utført, data_utført)






