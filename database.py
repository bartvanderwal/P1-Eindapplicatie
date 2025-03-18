"""Database component voor Eindapplicatie voor P1"""
import sqlite3

def connect_to_database():
    """Functie om verbinding te maken met database"""
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    # voor het geval dit de eerste keer is, anders doen de statements niets
    cursor.execute('CREATE TABLE IF NOT EXISTS person (name TEXT, afstand REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS hobby (name TEXT, hobby TEXT)')
    return cursor

def disconnect_from_database(db):
    """Functie om verbinding met database te verbreken (inlusief commit)"""
    db.connection.commit()
    db.close()

def person_exists_in_database(name):
    """Functie om  te controleren of persoon in de database bestaat"""
    db = connect_to_database()
    db.execute('SELECT name FROM person WHERE name = ?', (name,))
    row = db.fetchone()
    disconnect_from_database(db)
    return row is not None

def person_with_hobby_exists_in_database(name, hobby):
    """Functie om te controleren of persoon met hobby in de database bestaat"""
    db = connect_to_database()
    db.execute('SELECT name FROM hobby WHERE name = ? and hobby = ?', (name, hobby))
    row = db.fetchone()
    disconnect_from_database(db)
    return row is not None

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

def empty_database():
    """Functie om database te legen"""
    db = connect_to_database()
    db.execute('DELETE FROM hobby')
    db.execute('DELETE FROM person')
    disconnect_from_database(db)
    print("Database geleegd.")
