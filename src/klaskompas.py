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
'''UI component (en startpunt) van de Eindapplicatie voor P1'''
import persoonsbeheer
import hobbybeheer
import visualisatie

def main():
    '''Startpunt van de applicatie'''
    while True:
        print('Menu:')
        print('1. Vul database met data uit CSV-bestand (namen en afstanden)')
        print('2. Voeg hobby toe voor persoon')
        print('3. Werk afstand bij voor persoon')
        print('4. Verwijder hobby voor persoon')
        print('5. Toon grafiek met afstand per persoon')
        print('6. Print hobby\'s per persoon')
        print('7. Leeg database (alle data verwijderen)')
        print('8. Stop')

        keuze = input('Kies een optie: ')

        if keuze == '1':
            persoonsbeheer.importeer_personen_in_database()
        elif keuze == '2':
            naam = input('Voer naam in: ')
            hobby = input('Voer hobby in: ')
            hobbybeheer.voeg_hobby_toe_aan_database_als_persoon_aanwezig(naam, hobby)
        elif keuze == '3':
            naam = input('Voer naam in van de persoon die u wilt bijwerken: ')
            nieuwe_afstand = float(input('Voer nieuwe afstand in: '))
            persoonsbeheer.wijzig_afstand_in_database(naam, nieuwe_afstand)
        elif keuze == '4':
            naam = input('Voer naam in van record dat u wilt verwijderen: ')
            hobby = input('Voer hobby in van record dat u wilt verwijderen: ')
            hobbybeheer.verwijder_hobby_uit_database_indien_aanwezig(naam, hobby)
        elif keuze == '5':
            subkeuze = input('Wilt u een verticale (1) of horizontale (2) grafiek? ')
            if subkeuze == '1':
                visualisatie.toon_verticaal_staafdiagram()
            elif subkeuze == '2':
                maximum_staaflengte = int(input('Voer maximale lengte van balk in: '))
                karakter = input('Voer karakter in voor de grafiek (bijv. * of #): ')
                visualisatie.toon_horizontaal_staafdiagram(maximum_staaflengte, karakter)
            else:
                print('Ongeldige keuze. Probeer opnieuw.')
        elif keuze == '6':
            hobbybeheer.print_hobbys_aanwezig_in_database()
        elif keuze == '7':
            persoonsbeheer.verwijder_alle_personen_uit_database()
        elif keuze == '8':
            break
        else:
            print('Ongeldige keuze. Probeer opnieuw.')

if __name__ == '__main__':
    main()
