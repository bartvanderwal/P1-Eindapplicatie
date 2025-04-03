'''Visualisatie-component voor de P1 Eindapplicatie'''
import matplotlib.pyplot as plt
import database

def toon_verticaal_staafdiagram():
    '''Functie om data uit database te halen en als staafdiagram te tonen'''
    db = database.haal_databaseverbinding_op()
    db.execute('SELECT naam, afstand FROM persoon')
    rijen = db.fetchall()

    namen = [rij[0] for rij in rijen]  # misschien te shorthand voor P1
    afstanden = [rij[1] for rij in rijen]
    database.verbreek_verbinding_met_database(db)

    plt.bar(namen, afstanden)
    plt.xlabel('Naam')
    plt.xticks(rotation=45)
    plt.ylabel('Afstand')
    plt.title('Afstand per persoon')
    plt.show()

def toon_horizontaal_staafdiagram(maximale_staaflengte, karakter):
    '''Functie om data uit database te halen en als staafdiagram te tonen met ASCII-art'''
    db = database.haal_databaseverbinding_op()
    db.execute('SELECT naam, afstand FROM persoon')
    rijen = db.fetchall()

    grootste_afstand = max([row[1] for row in rijen]) # eventueel zelf uitprogrammeren
    lengte_van_langste_naam = max([len(row[0]) for row in rijen]) # eventueel zelf uitprogrammeren

    # optie om dit in een functie te zetten, zodat ze met decompositie kunnen oefenen
    for rij in rijen:
        naam = rij[0]
        afstand = rij[1]
        staaflengte = round(maximale_staaflengte * afstand / grootste_afstand)
        print(naam, end='')
        for _ in range(0, lengte_van_langste_naam - len(naam)):
            print(' ', end='')
        print('|')
        print(karakter * staaflengte)

    database.verbreek_verbinding_met_database(db)
