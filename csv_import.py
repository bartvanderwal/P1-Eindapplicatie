"""CSV Import component voor Eindapplicatie voor P1"""

import csv
import sqlite3
from database import person_exists_in_database

def read_data_from_csv(file_path):
    """Functie om data uit CSV-bestand te lezen"""
    data = []
    with open(file_path, 'r') as file: #utf-8 encoding eigenlijk toevoegen, is dat iets voor P1?
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def save_person_data_to_database(db_name, data):
    """Functie om persoonsdata (naam, afstand) in SQLite-database op te slaan"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for row in data:
        name=row[0]
        distance=float(row[1])
        if person_exists_in_database(db_name, name):
            print("Persoon " + name + " bestaat al in database.")
        else:
            cursor.execute('INSERT INTO person VALUES (?, ?)', (name, distance))

    conn.commit()
    conn.close()
