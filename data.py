"""Eindapplicatie voor P1"""
# Overwegingen/nog over nadenken:
# - Nu geen check of afstand wel een float is, dat zou kunnen met try/except
#   (maar dat is denk ik niet wenselijk) of met het trucje waarbij je de punt
#   verwijdert en dan kijkt of het een numeric is (maar ook dat lijkt me niet wenselijk).
# - Meldingen (zowel bevestigingen als foutmeldingen) zitten nu in de functies.
#   Dat is niet heel handig, maar anders ontkom je bijna niet aan try/except.
# - Elke functie die de database gebruikt opent en sluit de connectie. Je zou
#   kunnen overwegen de connectie globaal te maken en te sluiten bij het
#   afsluiten van het programma. Gezien het beperkte nadeel van deze oplossing
#   en het risico van het alternatief moet dit wellicht zo blijven.
# - inquirer gebruiken voor menu's? Is wel heel mooi, maar misschien te complex.
# - Iets met data-aggregatie toevoegen of eenvoudige berekeningen?
# - Algoritmiek ontbreekt nagenoeg.
# - Wat meer complexiteit in parameters en return values zou goed zijn, daar
#   moeten ze mee oefenen.


import csv
import sqlite3
import matplotlib.pyplot as plt


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

def create_distance_bar_chart(db_name):
    """Functie om data uit database te halen en als grafiek te tonen"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT name, afstand FROM person')
    rows = cursor.fetchall()

    names = [row[0] for row in rows]  # misschien te shorthand voor P1
    distances = [row[1] for row in rows]

    plt.bar(names, distances)
    plt.xlabel('Naam')
    plt.xticks(rotation=45)
    plt.ylabel('Afstand')
    plt.title('Afstand per persoon')
    plt.show()

def create_vertical_distance_bar_chart(db_name, max_bar_width, character):
    """Functie om data uit database te halen en als grafiek te tonen met ASCII-art"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('SELECT name, afstand FROM person')
    rows = cursor.fetchall()

    max_distance = max([row[1] for row in rows]) # eventueel zelf uitprogrammeren
    length_of_longest_name = max([len(row[0]) for row in rows]) # eventueel zelf uitprogrammeren

    for row in rows: # optie om dit in een functie te zetten, zodat ze met decompositie kunnen oefenen
        name = row[0]
        distance = row[1]
        bar_length = int(max_bar_width * distance / max_distance) # misschien te ingewikkeld?
        print(name, end='')
        for i in range(0, length_of_longest_name - len(name)):
            print(' ', end='')
        print('|' + character * bar_length)

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

def empty_database(db_name):
    """Functie om database te legen"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM hobby')
    cursor.execute('DELETE FROM person')
    conn.commit()
    conn.close()
    print("Database geleegd.")

def main():
    DB_NAME = 'data.db'
    CSV_FILE = 'data/data.csv'
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS person (name TEXT, afstand REAL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS hobby (name TEXT, hobby TEXT)')

    while True:
        print("Menu:")
        print("1. Vul database met data uit CSV-bestand (namen en afstanden)")
        print("2. Voeg hobby toe voor persoon")
        print("3. Werk afstand bij voor persoon")
        print("4. Verwijder hobby voor persoon")
        print("5. Toon grafiek met afstand per persoon")
        print("6. Print hobby's per persoon")
        print("7. Leeg database (alle data verwijderen)")
        print("8. Stop")

        choice = input("Kies een optie: ")

        if choice == '1':
            data = read_data_from_csv(CSV_FILE)
            save_person_data_to_database(DB_NAME, data)
        elif choice == '2':
            name = input("Voer naam in: ")
            hobby = input("Voer hobby in: ")
            add_hobby_to_database(DB_NAME, name, hobby)
        elif choice == '3':
            name = input("Voer naam in van de persoon die u wilt bijwerken: ")
            new_distance = float(input("Voer nieuwe afstand in: "))
            update_distance_in_database(DB_NAME, name, new_distance)
        elif choice == '4':
            name = input("Voer naam in van record dat u wilt verwijderen: ")
            hobby = input("Voer hobby in van record dat u wilt verwijderen: ")
            delete_hobby_from_database(DB_NAME, name, hobby)
        elif choice == '5':
            subchoice = input("Wilt u een verticale (1) of horizontale (2) grafiek? ")
            if subchoice == '1':
                create_distance_bar_chart(DB_NAME)
            elif subchoice == '2':
                max_bar_length = int(input("Voer maximale lengte van balk in: "))
                character = input("Voer karakter in voor de grafiek (bijv. * of #): ")
                create_vertical_distance_bar_chart(DB_NAME, max_bar_length, character)
            else:
                print("Ongeldige keuze. Probeer opnieuw.")
        elif choice == '6':
            print_hobbies_from_database(DB_NAME)
        elif choice == '7':
            empty_database(DB_NAME)
        elif choice == '8':
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == '__main__':
    main()