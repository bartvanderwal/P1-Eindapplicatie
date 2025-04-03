"""Hobby Management component van de P1 Eindapplicatie"""
import database

def voeg_hobby_toe_aan_database(naam, hobby):
    """Voegt een hobby toe aan de database zonder controles."""
    db = database.haal_databaseverbinding_op()
    db.execute('INSERT INTO hobby VALUES (?, ?)', (naam, hobby))
    database.verbreek_verbinding_met_database(db)

def voeg_hobby_toe_aan_database_als_persoon_aanwezig(naam, hobby):
    """Controleert of de persoon bestaat en voegt de hobby toe indien mogelijk."""
    if not database.persoon_aanwezig_in_database(naam):
        print("Persoon niet gevonden in database.")
    elif len(hobby) > 75:
        print("Hobbynaam is te lang, maximaal 75 karakters zijn toegestaan.")
    else:
        voeg_hobby_toe_aan_database(naam, hobby)
        print("Hobby toegevoegd aan database.")

def verwijder_hobby_uit_database(naam, hobby):
    """Functie om record te verwijderen uit database"""
    db = database.haal_databaseverbinding_op()
    db.execute('DELETE FROM hobby WHERE naam = ? and hobby = ?', (naam, hobby))
    database.verbreek_verbinding_met_database(db)

def verwijder_hobby_uit_database_indien_aanwezig(naam, hobby):
    """Controleert of een persoon de hobby heeft en verwijdert deze indien nodig."""
    if database.persoon_hobby_combinatie_aanwezig_in_database(naam, hobby):
        verwijder_hobby_uit_database(naam, hobby)
        print("Combinatie persoon en hobby verwijderd uit database.")
    else:
        print("Combinatie van persoon en hobby niet gevonden in database.")

def print_hobbys_aanwezig_in_database():
    """Functie om data uit database te halen en te printen"""
    db = database.haal_databaseverbinding_op()
    db.execute('SELECT naam, hobby FROM hobby ORDER BY naam')
    rijen = db.fetchall()

    for rij in rijen:
        naam = rij[0]
        hobby = rij[1]
        print(naam, hobby)

    database.verbreek_verbinding_met_database(db)

def verwijder_alle_hobbys_uit_database():
    """Functie om alle hobby's uit de database te verwijderen"""
    db = database.haal_databaseverbinding_op()
    db.execute('DELETE FROM hobby')
    database.verbreek_verbinding_met_database(db)
    print("Alle hobby's verwijderd uit database.")
