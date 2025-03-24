"""Hobby Management component van de P1 Eindapplicatie"""
from database import person_exists_in_database, person_with_hobby_exists_in_database, \
    connect_to_database, disconnect_from_database

def person_exists(name):
    """Controleert of een persoon in de database bestaat."""
    return person_exists_in_database(name)

def insert_hobby_into_database(name, hobby):
    """Voegt een hobby toe aan de database zonder controles."""
    db = connect_to_database()
    db.execute('INSERT INTO hobby VALUES (?, ?)', (name, hobby))
    disconnect_from_database(db)

def add_hobby_if_person_exists(name, hobby):
    """Controleert of de persoon bestaat en voegt de hobby toe indien mogelijk."""
    if not person_exists(name):
        print("Persoon niet gevonden in database.")
    elif len(hobby) > 75:
        print("Hobbynaam is te lang, maximaal 75 karakters zijn toegestaan.")
    else:
        insert_hobby_into_database(name, hobby)
        print("Hobby toegevoegd aan database.")

def delete_hobby_from_database(name, hobby):
    """Functie om record te verwijderen uit database"""
    db = connect_to_database()
    db.execute('DELETE FROM hobby WHERE name = ? and hobby = ?', (name, hobby))
    disconnect_from_database(db)
    print("Combinatie persoon en hobby verwijderd uit database.")

def remove_hobby_if_exists(name, hobby):
    """Controleert of een persoon de hobby heeft en verwijdert deze indien nodig."""
    if person_with_hobby_exists_in_database(name, hobby):
        delete_hobby_from_database(name, hobby)
        print("Combinatie persoon en hobby verwijderd uit database.")
    else:
        print("Combinatie van persoon en hobby niet gevonden in database.")

def print_hobbies_from_database():
    """Functie om data uit database te halen en te printen"""
    db = connect_to_database()
    db.execute('SELECT name, hobby FROM hobby ORDER BY name')
    rows = db.fetchall()

    for row in rows:
        name = row[0]
        hobby = row[1]
        print(name, hobby)

    disconnect_from_database(db)
