# Toetsvragen

## Enkele quotes of dubbele quotes?

Python staat bij gebruik strings zowel enkele als dubbele quotes toe. De PEP8 standaard geeft aan dit dan wel consistent binnen je codebase te doen. Bij gebruik van letterlijke quotes in je weer te geven tekst, kun je voor de 'string quotes' dan enkele quotes gebruiken als er dubbele quotes in de tekst voor komen. En enkele quotes als . Meestal zal dit niet voorkomen. Dan is het handig als er een default keuze is.

We gebruiken in Python liefst enkele quotes. Omdat in P2 een webapplicatie maken, en je daarbij HTML soms met Python code samenstelt. HTML gebruikt dubbele quotes in tags, zoals

```html
<p id="quote">
```

Echter geldt tegelijkertijd ook dat IN SQL queries, strings met enkele quotes zijn. En deze stel je ook samen.

```sql
    SELECT naam, GROUP_CONCAT(hobby, ', ') AS hobbies FROM hobby GROUP BY naam ORDER BY naam
```

Merk op dat het scheidingsteken voor de GROUP_CONCAT namelijk komma (,) hier als string opgeeft in SQL met enkele quotes eromheen: ``,``. Als je deze SQL in Python code verwerkt, zoals in onderstaande `db.execute` statement dan moet je de enkele quotes escapen met een forward slash ervoor. Omdat Python het anders ziet als afsluiting van de string die je db.execute geeft in plaats van het door te geven naar de database.

```python
    db.execute('SELECT naam, GROUP_CONCAT(hobby, \', \') AS hobbies FROM hobby GROUP BY naam ORDER BY naam')
```

### GROUP_CONCAT in Python code

```python
db = database.haal_databaseverbinding_op()
db.execute('SELECT naam, hobby FROM hobby ORDER BY naam')
rijen = db.fetchall()

# Vooraf: lijst om naam + hobbies op te slaan
groepjes = []

for naam, hobby in rijen:
    gevonden = False
    for persoon in groepjes:
        if persoon[0] == naam:
            persoon[1].append(hobby)
            gevonden = True
            break
    if not gevonden:
        groepjes.append([naam, [hobby]])

# Print netjes per persoon
for naam, hobbies in groepjes:
    print(f"{naam}: {', '.join(hobbies)}")

database.verbreek_verbinding_met_database(db)
```

