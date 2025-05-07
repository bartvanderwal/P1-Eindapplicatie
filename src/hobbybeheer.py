'''Hobby Management component van de P1 Eindapplicatie'''
import database
import persoonsbeheer


def voeg_hobby_toe_aan_database(naam, hobby):
    '''Voegt een hobby toe aan de database zonder controles.'''
    db = database.haal_databaseverbinding_op()
    db.execute('INSERT INTO hobby VALUES (?, ?)', (naam, hobby))
    database.verbreek_verbinding_met_database(db)


def voeg_hobby_toe_aan_database_als_persoon_aanwezig(naam, hobby):
    '''Controleert of de persoon bestaat en voegt de hobby toe indien mogelijk.'''
    if not persoonsbeheer.persoon_aanwezig_in_database(naam):
        print('Persoon niet gevonden in database.')
    elif len(hobby) > 75:
        print('Hobbynaam is te lang, maximaal 75 karakters zijn toegestaan.')
    else:
        voeg_hobby_toe_aan_database(naam, hobby)
        print('Hobby toegevoegd aan database.')


def verwijder_hobby_uit_database(naam, hobby):
    '''Functie om hobby record te verwijderen uit database'''
    db = database.haal_databaseverbinding_op()
    db.execute('DELETE FROM hobby WHERE naam = ? and hobby = ?', (naam, hobby))
    database.verbreek_verbinding_met_database(db)


def verwijder_hobby_uit_database_indien_aanwezig(naam, hobby):
    '''Controleert of een persoon de hobby heeft en verwijdert deze indien nodig.'''
    if persoonsbeheer.persoon_hobby_combinatie_aanwezig_in_database(naam, hobby):
        verwijder_hobby_uit_database(naam, hobby)
        print('Combinatie persoon en hobby verwijderd uit database.')
    else:
        print('Combinatie van persoon en hobby niet gevonden in database.')


def print_hobbys_aanwezig_in_database():
    '''Functie om alle student hobby data uit database te halen en te printen'''

    db = database.haal_databaseverbinding_op()
    db.execute('SELECT naam, GROUP_CONCAT(hobby, \', \') AS hobbies FROM hobby GROUP BY naam ORDER BY naam')
    rijen = db.fetchall()

    if len(rijen) == 0:
        print('Geen hobby\'s in database.')
    else:
        print('Hobby\'s in database:')
        for naam, hobbies in rijen:
            print(naam + ': ', hobbies)

    database.verbreek_verbinding_met_database(db)


def print_alle_unieke_hobbies():
    '''Functie om alle unieke hobby's in de database te printen ongeacht de student'''
    db = database.haal_databaseverbinding_op()
    db.execute('SELECT DISTINCT hobby FROM hobby ORDER BY hobby')
    rijen = db.fetchall()
    if len(rijen) == 0:
        print('Geen hobby\'s in database.')
    else:
        print('Hobby\'s in database:')
        for hobby in rijen:
            print(hobby[0])
    database.verbreek_verbinding_met_database(db)

def samenvoegen_hobby(samen_te_voegen, samenvoegen_met):
    '''Functie om alle unieke hobby's in de database te printen ongeacht de student'''
    db = database.haal_databaseverbinding_op()
    hobbies_result = db.execute('SELECT DISTINCT hobby FROM hobby ORDER BY hobby').fetchall()
    hobbies = [r[0] for r in hobbies_result]  # lijst van strings

    if samen_te_voegen == samenvoegen_met:
        print('Hobby\'s zijn gelijk, niets te doen.')
        return
    if samen_te_voegen not in hobbies:
        print('Hobby om te migreren niet gevonden in database.')
        return
    if samenvoegen_met not in hobbies:
        print('Hobby om naar te migreren niet gevonden in database.')
        return
    db.execute('UPDATE hobby SET hobby = ? WHERE hobby = ?', (samenvoegen_met, samen_te_voegen))
    database.verbreek_verbinding_met_database(db)
    print('Hobby\'s samengevoegd in database.')

def verwijder_alle_hobbys_uit_database():
    '''Functie om alle hobby's uit de database te verwijderen'''
    db = database.haal_databaseverbinding_op()
    db.execute('DELETE FROM hobby')
    database.verbreek_verbinding_met_database(db)
    print('Elke hobby verwijderd uit database.')
