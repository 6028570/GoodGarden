# GoodGarden

Welkom bij ons project genaamd "GoodGarden". Wij hebben besloten om er een semi-monolithic project van te maken. Alles is te vinden binnen deze repository, inclusief de "mqtt" publisher.

### Vereisten

 * Python
 * Node.Js
 * XAMPP (of andere naar keuze)
 * MQTT Geinstalleerd en toegevoegd aan je PATH variable

### Installeren

Zorg dat je in de hoofdmap "GoodGarden" zit. Kijk in je path: "../GoodGarden". Als je in de correcte map zit moet je de volgende items installeren:

     npm install electron
     npm install express
     npm install body-parser
     npm install python-shell

     npm install --save-dev npm-run-all
     npm install wait-on --save-dev
     npm install concurrently --save-dev
     
     
     pip install mysql-connector-python
     pip install requests
     pip install flask-cors
     pip install Flask-SQLAlchemy

## Gebruik

- De data wordt gefetched via MQTT, waarnaar het in topics wordt verdeeld en dan kan je met een script op he gewenste onderwerp "subscriben". 

- Op het Dashboard worden de planten getoond die aanwezig zijn in de database. Je kan doormiddel een modal de planten invullen die je getoond wilt hebben op het Dashboard. Voor nu moet je dan even het "planten.py" script handmatig uitvoeren. Ook worden de 2 sensoren getoond op het Dashboard en hebben we voor nu een "placeholder" neergezet voor de pomp.

- Als je op een plant klikt ga je naar de pagina van de plant toe. Die is dynamisch gemaakt, alleen nog niet helemaal ingevuld met data. Er zit een switch-knop in waarmee je kan aangeven of de plant aanwezig is in de kas of niet, ook die werkt helaas niet helemaal naar behoren.

- Je kan ook op de sensoren klikken die op de homepage staan. Dan ga je door naar de pagina van die desbetreffende sensor. De bedoeling was om hier alle errors en waardes te tonen de we doorkrijgen van de sensoren.

- Als laatste hebben we een grafiek toegevoegd aan het project die laat zien wat de temperatuur is voor de aankomende 5 dagen. De bedoeling was om voor elke plant een unieke grafiek te maken waar dan data in getoond zou worden.

## Versiebeheer

We gebruiken [Github](https://github.com) voor versiebeheer. Voor de beschikbare versies, zie de [GoodGarden](https://github.com/6028570/GoodGarden).

De branch "oomen" is up to date. Het mergen ging niet helemaal goed dus we hebben het niet met  "main" gemerged.

## Auteurs

* **Atilla Oomen** - *Projectleider | Back end Programmeur* - [Znooptokkie](https://github.com/Znooptokkie)

* **Mohammed Çifçi** - *Back end Programmeur* - [6028570](https://github.com/6028570)

* **Burak Diker** - *Back end Programmeur* - [6028083](https://github.com/6028083)

* **Justin Doekhi** - *Front end Programmeur* - [6027529](https://github.com/6027529)

* **Renzo van Putten** - *Front end Programmeur* - [6025850](https://github.com/6025850)