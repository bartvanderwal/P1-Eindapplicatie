'''Database component voor Eindapplicatie voor P1'''
import sqlite3
import persoonsbeheer
import hobbybeheer
import csv


def haal_databaseverbinding_op():
    '''Functie om verbinding te maken met database'''
    connectie = sqlite3.connect('db/data.db', autocommit=True)

    # feitelijk gebruiken we een cursor, maar we gebruiken het als een databaseverbinding
    db = connectie.cursor()

    # voor het geval dit de eerste keer is, anders doen de statements niets
    db.execute('''CREATE TABLE IF NOT EXISTS persoon (
                        naam TEXT NOT NULL PRIMARY KEY,
                        afstand NUMERIC(3,1) NOT NULL
                     )''')
    db.execute('''CREATE TABLE IF NOT EXISTS hobby (
                        naam TEXT NOT NULL,
                        hobby TEXT NOT NULL,
                        PRIMARY KEY(naam, hobby),
                        FOREIGN KEY(naam) REFERENCES persoon(naam)
                     )''')
    return db


def verbreek_verbinding_met_database(db):
    '''Functie om verbinding met database te verbreken'''
    db.close()

def importeer_data():
    '''Functie om data uit CSV-bestand te lezen en in de database te importeren'''
    db = haal_databaseverbinding_op()
    data = list()

    # utf-8 encoding eigenlijk toevoegen, is dat iets voor P1?
    with open('data/data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for rij in csv_reader:
            data.append(rij)
    
    for persoon in data:
        # Controleer of de persoon al in de database staat
        if persoonsbeheer.persoon_aanwezig_in_database(data[0]):
            print('Persoon ' + data[0] + ' bestaat al in database.')
        else:
            # Voeg de persoon toe aan de database
            naam_en_afstand = data[:2];
            persoonsbeheer.voeg_persoon_toe_aan_database(*naam_en_afstand)
    
            # Splits eventuele hobby string zoals "hobby1, hobby2" op in een lijst van strings "hobby1"
            hobbies = data[2].split(",")
            for hobby in hobbies:
                if persoonsbeheer.persoon_hobby_combinatie_aanwezig_in_database(data[0], hobby):
                    print('Persoon ' + data[0] + ' met hobby ' + hobby + ' bestaat al in database.')
                else:
                    hobbybeheer.voeg_hobby_toe_aan_database(persoon, hobby=hobby)
        
        print('Data geïmporteerd uit CSV-bestand.')

    verbreek_verbinding_met_database(db)