'''Database component voor Eindapplicatie voor P1'''
import sqlite3

def haal_databaseverbinding_op():
    '''Functie om verbinding te maken met database'''

    # isolation_level=None zorgt ervoor dat de database in autocommit mode is
    connectie = sqlite3.connect('db/data.db', isolation_level=None)
        
    # feitelijk gebruiken we een cursor, maar we gebruiken het als een databaseverbinding
    db = connectie.cursor()

    # voor het geval dit de eerste keer is, anders doen de statements niets
    db.execute('''CREATE TABLE IF NOT EXISTS persoon (
                        naam VARCHAR(50) PRIMARY KEY, 
                        afstand NUMERIC(3,1)
                     )''')
    db.execute('''CREATE TABLE IF NOT EXISTS hobby (
                        naam VARCHAR(50), 
                        hobby VARCHAR(75), 
                        PRIMARY KEY(naam, hobby), 
                        FOREIGN KEY(naam) REFERENCES persoon(naam)
                     )''')
    return db

def verbreek_verbinding_met_database(db):
    '''Functie om verbinding met database te verbreken'''
    db.close()

def persoon_aanwezig_in_database(naam):
    '''Functie om  te controleren of persoon in de database bestaat'''
    db = haal_databaseverbinding_op()
    db.execute('SELECT naam FROM persoon WHERE naam = ?', (naam,))
    row = db.fetchone()
    verbreek_verbinding_met_database(db)
    return row is not None

def persoon_hobby_combinatie_aanwezig_in_database(naam, hobby):
    '''Functie om te controleren of persoon met hobby in de database bestaat'''
    db = haal_databaseverbinding_op()
    db.execute('SELECT naam FROM hobby WHERE naam = ? and hobby = ?', (naam, hobby))
    row = db.fetchone()
    verbreek_verbinding_met_database(db)
    return row is not None
