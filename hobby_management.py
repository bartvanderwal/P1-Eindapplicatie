"""Hobby Management component van de P1 Eindapplicatie"""
from database import person_exists_in_database, person_with_hobby_exists_in_database, \
    connect_to_database, disconnect_from_database

def add_hobby_to_database(name, hobby):
    """Functie om record toe te voegen aan database"""
    if not person_exists_in_database(name):
        print ("Persoon niet gevonden in database.")
    else:
        db = connect_to_database()
        db.execute('INSERT INTO hobby VALUES (?, ?)', (name, hobby))
        disconnect_from_database(db)
        print("Hobby toegevoegd aan database.")

def delete_hobby_from_database(name, hobby):
    """Functie om record te verwijderen uit database"""
    if not person_with_hobby_exists_in_database(name, hobby):
        print("Combinatie van persoon en hobby niet gevonden in database.")
    else:
        db = connect_to_database()
        db.execute('DELETE FROM hobby WHERE name = ? and hobby = ?', (name, hobby))
        disconnect_from_database(db)
        print("Combinatie persoon en hobby verwijderd uit database.")

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
