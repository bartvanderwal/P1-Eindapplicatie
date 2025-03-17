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
"""UI component (en startpunt) van de Eindapplicatie voor P1"""
import sqlite3
from csv_import import read_data_from_csv, save_person_data_to_database
from database import empty_database, update_distance_in_database
from hobby_management import add_hobby_to_database, delete_hobby_from_database, print_hobbies_from_database
from visualisation import create_distance_bar_chart, create_vertical_distance_bar_chart

def main():
    """Startpunt van de applicatie"""
    db_name = 'data.db'
    csv_file = 'data/data.csv'
    conn = sqlite3.connect(db_name)
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
            data = read_data_from_csv(csv_file)
            save_person_data_to_database(db_name, data)
        elif choice == '2':
            name = input("Voer naam in: ")
            hobby = input("Voer hobby in: ")
            add_hobby_to_database(db_name, name, hobby)
        elif choice == '3':
            name = input("Voer naam in van de persoon die u wilt bijwerken: ")
            new_distance = float(input("Voer nieuwe afstand in: "))
            update_distance_in_database(db_name, name, new_distance)
        elif choice == '4':
            name = input("Voer naam in van record dat u wilt verwijderen: ")
            hobby = input("Voer hobby in van record dat u wilt verwijderen: ")
            delete_hobby_from_database(db_name, name, hobby)
        elif choice == '5':
            subchoice = input("Wilt u een verticale (1) of horizontale (2) grafiek? ")
            if subchoice == '1':
                create_distance_bar_chart(db_name)
            elif subchoice == '2':
                max_bar_length = int(input("Voer maximale lengte van balk in: "))
                character = input("Voer karakter in voor de grafiek (bijv. * of #): ")
                create_vertical_distance_bar_chart(db_name, max_bar_length, character)
            else:
                print("Ongeldige keuze. Probeer opnieuw.")
        elif choice == '6':
            print_hobbies_from_database(db_name)
        elif choice == '7':
            empty_database(db_name)
        elif choice == '8':
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == '__main__':
    main()
