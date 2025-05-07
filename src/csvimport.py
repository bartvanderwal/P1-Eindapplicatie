'''CVS import component voor Eindapplicatie voor P1'''
import csv

import persoonsbeheer
import hobbybeheer

def _verwerk_persoon(persoon):
    '''Private methode om persoon en zijn hobby's te verwerken en op te slaan'''
    # Controleer of de persoon al in de database staat
    naam = persoon[0]
    if persoonsbeheer.persoon_aanwezig_in_database(naam):
        print('Persoon ' + naam + ' bestaat al in database.')
    else:
        # Voeg de persoon toe aan de database
        naam_en_afstand = persoon[:2]
        persoonsbeheer.voeg_persoon_toe_aan_database(naam_en_afstand)

    # Splits eventuele hobby string op in een lijst van strings
    # Bijvoorbeeld "hobby1, hobby2" op ["hobby1", "hobby2"].
    hobbies = persoon[2]
    if hobbies == '':
        print('Geen hobby\'s opgegeven voor ' + naam)
    else:
        hobbies = persoon[2].split(", ")
        print('Hobby\'s van ' + naam + ' gesplit: ', hobbies)
        for hobby in hobbies:
            if persoonsbeheer.persoon_hobby_combinatie_aanwezig_in_database(naam, hobby):
                print('Persoon ' + persoon[0] + ' met hobby ' + hobby + ' bestaat al in database.')
            else:
                hobbybeheer.voeg_hobby_toe_aan_database(naam, hobby)

    print('Data geïmporteerd uit CSV-bestand.')

def importeer_data():
    '''Functie om data uit CSV-bestand te lezen en in de database te importeren'''
    data = []

    # utf-8 encoding eigenlijk toevoegen, is dat iets voor P1?
    with open('data/data.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for rij in csv_reader:
            data.append(rij)
            # Strip eventuele spaties en newline tekens in alle kolommen het invoerbestand 
            # (te ingewikkeld met lijst comprehensie en iterator)
            # data.append([kol.strip() for kol in rij])

    for persoon in data:
        for persoon in data:
            _verwerk_persoon(persoon)
