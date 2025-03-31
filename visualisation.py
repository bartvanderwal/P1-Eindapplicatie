"""Visualisation component voor de P1 Eindapplicatie"""
import matplotlib.pyplot as plt
from database import connect_to_database, disconnect_from_database

def create_distance_bar_chart():
    """Functie om data uit database te halen en als grafiek te tonen"""
    db = connect_to_database()
    db.execute('SELECT name, afstand FROM person')
    rows = db.fetchall()

    names = [row[0] for row in rows]  # misschien te shorthand voor P1
    distances = [row[1] for row in rows]
    disconnect_from_database(db)

    plt.bar(names, distances)
    plt.xlabel('Naam')
    plt.xticks(rotation=45)
    plt.ylabel('Afstand')
    plt.title('Afstand per persoon')
    plt.show()

def create_vertical_distance_bar_chart(max_bar_width, character):
    """Functie om data uit database te halen en als grafiek te tonen met ASCII-art"""
    db = connect_to_database()
    db.execute('SELECT name, afstand FROM person')
    rows = db.fetchall()

    max_distance = max([row[1] for row in rows]) # eventueel zelf uitprogrammeren
    length_of_longest_name = max([len(row[0]) for row in rows]) # eventueel zelf uitprogrammeren

    # optie om dit in een functie te zetten, zodat ze met decompositie kunnen oefenen
    for row in rows:
        name = row[0]
        distance = row[1]
        bar_length = round(max_bar_width * distance / max_distance) # misschien te ingewikkeld?
        print(name, end='')
        for _ in range(0, length_of_longest_name - len(name)):
            print(' ', end='')
        print('|' + character * bar_length)

    disconnect_from_database(db)
