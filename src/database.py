'''Database component voor Eindapplicatie voor P1'''
import sqlite3


def haal_databaseverbinding_op():
    '''Functie om verbinding te maken met database'''
    connectie = sqlite3.connect('db/data.db', autocommit=True)

    # feitelijk gebruiken we een cursor, maar we gebruiken het als een databaseverbinding
    db = connectie.cursor()

    # voor het geval dit de eerste keer is, anders doen de statements niets
    db.execute('''CREATE TABLE IF NOT EXISTS persoon (
                        naam VARCHAR(50) NOT NULL PRIMARY KEY, 
                        afstand NUMERIC(3,1)
                     )''')
    db.execute('''CREATE TABLE IF NOT EXISTS hobby (
                        naam VARCHAR(50) NOT NULL, 
                        hobby VARCHAR(75) NOT NULL, 
                        PRIMARY KEY(naam, hobby), 
                        FOREIGN KEY(naam) REFERENCES persoon(naam)
                     )''')
    return db


def verbreek_verbinding_met_database(db):
    '''Functie om verbinding met database te verbreken'''
    db.close()
