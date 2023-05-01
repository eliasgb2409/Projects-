import psycopg2

# MERK: Må kjøres med Python 3

user = 'eliasgb' # Sett inn ditt UiO-brukernavn ("_priv" blir lagt til under)
pwd = 'ohFu7thof0' # Sett inn passordet for _priv-brukeren du fikk i en mail

connection = \
    "dbname='" + user + "' " +  \
    "user='" + user + "_priv' " + \
    "port='5432' " +  \
    "host='dbpg-ifi-kurs03.uio.no' " + \
    "password='" + pwd + "'"

def huffsa():
    conn = psycopg2.connect(connection)

    ch = 0
    while (ch != 3):
        print("\n--[ HUFFSA ]--")
        print("Vennligst velg et alternativ:\n 1. Søk etter planet\n 2. Legg inn forsøksresultat\n 3. Avslutt")
        ch = int(input("Valg: "))

        if (ch == 1):
            planet_sok(conn)
        elif (ch == 2):
            legg_inn_resultat(conn)

def planet_sok(conn):

    #Ber om input fra bruker - input er to eller en molekyler
    print("\n---[ SØKER ETTER PLANET ]---")
    print("Oppgi minst et molekyl, maximum to. \n")
    molecule1 = input("Molekyl 1: ")
    molecule2 = input("Molekyl 2: ")

    #Definerer en spørring som henter ut
    #planetens navn, planetens masse, stjernens masse, stjernens avstand, planetens Liv
    #basert på om molekylet brukeren oppga har blitt oberservert på planeten
    q = f"(SELECT DISTINCT planet.navn, planet.masse, stjerne.masse, stjerne.avstand, planet.liv FROM planet " +\
    f"INNER JOIN materie ON (planet.navn = materie.planet) " +\
    f"INNER JOIN stjerne ON (planet.stjerne = stjerne.navn) " +\
    f"WHERE materie.molekyl = '{molecule1}')"

    #Legger til en spørring om brukeren oppga 2 molekyler - da skal begge molekyler ha blitt oppdaget på planeten
    #Bruker interesct for å finne planeter der både molecule1 og molecule2 finnes
    if molecule2 != "":
        q += f"INTERSECT (SELECT DISTINCT planet.navn, planet.masse, stjerne.masse, stjerne.avstand, planet.liv FROM planet " +\
        f"INNER JOIN materie ON (planet.navn = materie.planet) " +\
        f"INNER JOIN stjerne ON (planet.stjerne = stjerne.navn) " +\
        f"WHERE materie.molekyl = '{molecule2}')" #eller: WHERE materie.molekyl LIKE '{%molecule2}%'

    q += ";"

    #print(q)


    cur = conn.cursor()
    cur.execute(q)
    rows = cur.fetchall() # Retrieve all restults into a list of tuples

    if (rows == []):
        print("No results.")


    #sorted(rows, key=lambda L: tuple(float(el[3]) or '' for el in L), reverse=True)

    #rows = sorted(rows,key=lambda x:(-x[3] or '',x[0]), reverse=True)

    #Sorterer listen av tupler basert på indeks 3 (stjernens avstand)
    #Hvis indeks 3 er null så setter vi det i enden av sorteringen
    rows.sort(key = lambda x: (x[3] is None, x[3]))

    #Teller for antall rader som printes ut ved resultat
    n_rows = 0
    #Iterere gjennom alle resultatene
    #Hver rad er en liste med resultatsverdier fra sql spørringer
    #Disse kan vi hente ut basert på deres indeks i listen
    #Printer ut hvert resultat
    for row in rows:
        n_rows += 1
        navn = str(row[0])
        planet_masse = str(row[1])
        stjerne_masse = str(row[2])
        stjerne_distanse = str(row[3])
        liv = str(row[4])
        if liv == "True":
            liv = "Ja"
        elif liv == "False":
            liv = "Nei"
        print("\n" + "--- PLANET ---")
        print("Navn: " + navn + "\n" \
              "Planet-masse: " + planet_masse + "\n" + \
              "Stjerne-masse: " + stjerne_masse + "\n" + \
              "Stjerne-distanse: " + stjerne_distanse + "\n" + \
              "Liv: " + liv)


        #print(len(row))

    print(f"\nRows({n_rows})")



def legg_inn_resultat(conn):


    print("\n---[ LEGG INN NYTT RESULTAT ]---")
    # Motta input fra bruker om data som skal oppdateres
    planet_navn = input("Planet: ") #text
    skummel = input("Skummel: ") #boolean
    intelligent = input("Intelligent: ") #boolean
    beskrivelse = input("Beskrivelse: ") #text

    #Gjøre om input til boolske verdier for sql-spørringen
    if skummel == "j":
        skummel = "true"
    else:
        skummel = "false"

    if intelligent == "j":
        intelligent = "true"
    else:
        intelligent = "false"

    cur = conn.cursor() # Create a cursor object that can be used for executing queries

    # Kjører sql-spørring som oppdaterer planetens kolonne "skummel", "intelligent", "beskrivelse" og "liv"
    cur.execute(f"UPDATE planet SET skummel = '{skummel}', intelligent = '{intelligent}', beskrivelse = '{beskrivelse}', liv = 'true' WHERE navn = '{planet_navn}';")
    conn.commit()
    print("\n**Resultat lagt inn.**")



if __name__ == "__main__":
    huffsa()
