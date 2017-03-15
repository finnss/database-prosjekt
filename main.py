import mysql.connector
from create_data import add_user
from create_tables import execute_create_tables

config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'test_schema',
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def help():
    print('Følgende kommandoer er tilgjengelige:')
    print('0\tVis denne oversikten igjen')
    print('1\tGå til oppretting av treningsøkter og øvelser')
    print('2\tGå til oversikt over kjente treninger/øvelser')
    print('3\tGå til oppretting av mål')
    print('4\tGå til oversikt over kjente mål')
    print('5\tAvslutt')


def main():
    print('Velkommen til treningsdatabasen!')
    print('Dette programmet antar en lokal MySQL-database med navn')
    print('"test_schema" og brukernavn/passord lik "root/password".')
    newUser = input('Ny bruker? y/n ').lower() == 'y'

    if newUser:
        print('Oppretter bruker.')
        username = input('Vennligst oppgi brukernavn: ')
        gender = input('Vennligst oppgi kjønn(m/f/hva faen du vil): ')
        age = input('Vennligst oppgi alder: ')
        cursor.execute(add_user, (username, gender, age))
    else:
        username = input('Brukernavn: ')
    print('Logget inn.')

    if input('Opprette tabeller? y/n: ') == 'y':
        execute_create_tables(cursor, cnx)

    query = 0
    help()

    while query is not 5:
        print('Neste kommando (0 for hjelp):')
        query = int(input('> '))
        if query is 0:
            help()
        elif query is 1:
            print('Valgt: Gå til oppretting av treningsøkter og øvelser\n')
            # new_session()
        elif query is 2:
            print('Valgt: Gå til oversikt over kjente treninger/øvelser\n')
            # view_exercises()
        elif query is 3:
            print('Valgt: Gå til oppretting av mål\n')
            # create_goals()
        elif query is 4:
            print('Valgt: Gå til oversikt over kjente mål\n')
            # view_goals()
        elif query is 5:
            print('Valgt: Avslutt\n')
            print('Takk for nå!')
            break
        else:
            print('Ugylding input! Prøv igjen.')


main()

cnx.commit()
cursor.close()
cnx.close()