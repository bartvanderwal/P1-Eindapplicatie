"""Database component voor Eindapplicatie voor P1"""
import sqlite3

def person_exists_in_database(db_name, name):
    """Functie om  te controleren of persoon in de database bestaat"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM person WHERE name = ?', (name,))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def person_with_hobby_exists_in_database(db_name, name, hobby):
    """Functie om te controleren of persoon met hobby in de database bestaat"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM hobby WHERE name = ? and hobby = ?', (name, hobby))
    row = cursor.fetchone()
    conn.close()
    return row is not None

def update_distance_in_database(db_name, name, new_distance):
    """Functie om record bij te werken in database"""
    if not person_exists_in_database(db_name, name):
        print("Persoon niet gevonden in database.")
    elif new_distance < 0:
        print("Ongeldige waarde voor afstand.")
    else:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('UPDATE person SET afstand = ? WHERE name = ?', (new_distance, name))
        conn.commit()
        conn.close()
        print("Afstand bijgewerkt in database.")

def empty_database(db_name):
    """Functie om database te legen"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM hobby')
    cursor.execute('DELETE FROM person')
    conn.commit()
    conn.close()
    print("Database geleegd.")

