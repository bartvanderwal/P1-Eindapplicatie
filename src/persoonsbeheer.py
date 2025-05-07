'''CSV Import component voor Eindapplicatie voor P1'''

import database
import hobbybeheer


def persoon_aanwezig_in_database(naam):
    '''Functie om  te controleren of persoon in de database bestaat'''
    print('persoon_aanwezig_in_database: naam:', naam)

    db = database.haal_databaseverbinding_op()
    db.execute('SELECT naam FROM persoon WHERE naam = ?', (naam,))
    row = db.fetchone()
    database.verbreek_verbinding_met_database(db)
    return row is not None


def voeg_persoon_toe_aan_database(data):
    '''Functie om persoonsdata (naam, distance) in SQLite-database op te slaan'''
    print('voeg_persoon_toe_aan_database: data:', data)
    db = database.haal_databaseverbinding_op()

    naam = data[0]
    afstand = float(data[1])
    if persoon_aanwezig_in_database(naam):
        print('Persoon ' + naam + ' bestaat al in database.')
    else:
        db.execute('INSERT INTO persoon VALUES (?, ?)', (naam, afstand))

    database.verbreek_verbinding_met_database(db)


def wijzig_afstand_in_database(naam, nieuwe_afstand):
    '''Functie om record bij te werken in database'''
    if not persoon_aanwezig_in_database(naam):
        print('Persoon niet gevonden in database.')
    elif nieuwe_afstand <= 0:
        print('Ongeldige waarde voor afstand.')
    else:
        db = database.haal_databaseverbinding_op()
        db.execute('UPDATE persoon SET afstand = ? WHERE naam = ?',
                   (nieuwe_afstand, naam))
        database.verbreek_verbinding_met_database(db)
        print('Afstand bijgewerkt in database.')


def verwijder_alle_personen_uit_database():
    '''Functie om database te legen'''
    db = database.haal_databaseverbinding_op()
    hobbybeheer.verwijder_alle_hobbys_uit_database()
    db.execute('DELETE FROM persoon')
    database.verbreek_verbinding_met_database(db)
    print('Database geleegd.')


def persoon_hobby_combinatie_aanwezig_in_database(naam, hobby):
    '''Functie om te controleren of persoon met hobby in de database bestaat'''
    db = database.haal_databaseverbinding_op()
    db.execute(
        'SELECT naam FROM hobby WHERE naam = ? and hobby = ?', (naam, hobby))
    row = db.fetchone()
    database.verbreek_verbinding_met_database(db)
    return row is not None
