"""Hobby Management component van de P1 Eindapplicatie"""
import sqlite3
from database import person_exists_in_database, person_with_hobby_exists_in_database

def add_hobby_to_database(db_name, name, hobby):
    """Functie om record toe te voegen aan database"""
    if not person_exists_in_database(db_name, name):
        print ("Persoon niet gevonden in database.")
    else:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO hobby VALUES (?, ?)', (name, hobby))
        conn.commit()
        conn.close()
        print("Hobby toegevoegd aan database.")

def delete_hobby_from_database(db_name, name, hobby):
    """Functie om record te verwijderen uit database"""
    if not person_with_hobby_exists_in_database(db_name, name, hobby):
        print("Combinatie van persoon en hobby niet gevonden in database.")
    else:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM hobby WHERE name = ? and hobby = ?', (name, hobby))
        conn.commit()
        conn.close()
        print("Combinatie persoon en hobby verwijderd uit database.")

def print_hobbies_from_database(db_name):
    """Functie om data uit database te halen en te printen"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT name, hobby FROM hobby ORDER BY name')
    rows = cursor.fetchall()

    for row in rows:
        name = row[0]
        hobby = row[1]
        print(name, hobby)

    conn.close()
