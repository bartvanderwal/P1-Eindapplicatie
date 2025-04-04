'''Visualisatie-component voor de P1 Eindapplicatie'''
import matplotlib.pyplot as plt
import database


def toon_verticaal_staafdiagram():
    '''Functie om data uit database te halen en als staafdiagram te tonen'''
    db = database.haal_databaseverbinding_op()
    db.execute('SELECT naam, afstand FROM persoon')
    rijen = db.fetchall()

    namen = []
    afstanden = []
    for naam, afstand in rijen:
        namen.append(naam)
        afstanden.append(afstand)

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

    # eventueel zelf uitprogrammeren
    grootste_afstand = max([row[1] for row in rijen])
    # eventueel zelf uitprogrammeren
    lengte_van_langste_naam = max([len(row[0]) for row in rijen])

    # optie om dit in een functie te zetten, zodat ze met decompositie kunnen oefenen
    for naam, afstand in rijen:
        staaflengte = round(maximale_staaflengte * afstand / grootste_afstand)
        print(naam, end='')
        aantal_extra = lengte_van_langste_naam - len(naam)
        print(' ' * aantal_extra, end='')
        print('|', end='')
        print(karakter * staaflengte)

    database.verbreek_verbinding_met_database(db)
