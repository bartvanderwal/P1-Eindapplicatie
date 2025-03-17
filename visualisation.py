"""Visualisation component voor de P1 Eindapplicatie"""
import sqlite3
import matplotlib.pyplot as plt

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

    conn.close()
   