"""CSV Import component voor Eindapplicatie voor P1"""

import csv
from database import person_exists_in_database, connect_to_database, disconnect_from_database

def read_data_from_csv(file_path):
    """Functie om data uit CSV-bestand te lezen"""
    data = []
    with open(file_path, 'r') as file: #utf-8 encoding eigenlijk toevoegen, is dat iets voor P1?
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def save_person_data_to_database(data):
    """Functie om persoonsdata (naam, afstand) in SQLite-database op te slaan"""
    db = connect_to_database()

    for row in data:
        name=row[0]
        distance=float(row[1])
        if person_exists_in_database(name):
            print("Persoon " + name + " bestaat al in database.")
        else:
            db.execute('INSERT INTO person VALUES (?, ?)', (name, distance))

    disconnect_from_database(db)
