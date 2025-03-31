"""CSV Import component voor Eindapplicatie voor P1"""

import csv
from database import person_exists_in_database, connect_to_database, disconnect_from_database

def import_persons_to_database():
    """Functie om data uit CSV-bestand te lezen"""
    data = []
    #utf-8 encoding eigenlijk toevoegen, is dat iets voor P1?
    with open('data/data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    save_person_to_database(data)

def save_person_to_database(data):
    """Functie om persoonsdata (naam, distance) in SQLite-database op te slaan"""
    db = connect_to_database()

    for row in data:
        name=row[0]
        distance=float(row[1])
        if person_exists_in_database(name):
            print("Persoon " + name + " bestaat al in database.")
        else:
            db.execute('INSERT INTO person VALUES (?, ?)', (name, distance))

    disconnect_from_database(db)

def update_distance_in_database(name, new_distance):
    """Functie om record bij te werken in database"""
    if not person_exists_in_database(name):
        print("Persoon niet gevonden in database.")
    elif new_distance < 0:
        print("Ongeldige waarde voor afstand.")
    else:
        db = connect_to_database()
        db.execute('UPDATE person SET afstand = ? WHERE name = ?', (new_distance, name))
        disconnect_from_database(db)
        print("Afstand bijgewerkt in database.")

def delete_persons_from_database():
    """Functie om database te legen"""
    db = connect_to_database()
    db.execute('DELETE FROM hobby')
    db.execute('DELETE FROM person')
    disconnect_from_database(db)
    print("Database geleegd.")
