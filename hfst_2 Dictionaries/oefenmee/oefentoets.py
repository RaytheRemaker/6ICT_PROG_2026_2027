""" Oefening 2 (  / 6)
Het kassasysteem van een bistro houdt de openstaande rekeningen per tafel bij.
In deze oefening ga je bestellingen toevoegen of tafels laten afrekenen.

Herhaal het volgende tot de gebruiker 'STOP' ingeeft bij de tafelnaam:
    - Vraag naar de tafelnaam (bv. 'Tafel 1').
    - Vraag welke actie de kelner wil uitvoeren: 'bestellen' of 'afrekenen'.

voorraad = {
    "burgers": 12,
    "loempias": 8,
    "frikandellen": 5
}

while True:
    snack = input("Kies een product: ")

    if snack == "STOP": 
        break

    aantal = int(input("Hoeveel stuks (negatief = verkoop, positief = aankoop): "))

    if snack in voorraad:
        if voorraad[snack] + aantal < 0:
            print("Fout! Er zijn slechts", voorraad[snack], snack, "in voorraad.")
        else:
            voorraad[snack] = voorraad[snack] + aantal
            print("Er zijn nu", voorraad[snack], snack, "in voorraad.")
    else:
        if aantal < 0:
            print("Fout! Dit product bestaat nog niet.")
        else:
            voorraad[snack] = aantal
            print("Er zijn nu", voorraad[snack], snack, "in voorraad.")

print("De snackbar heeft volgende snacks op voorraad...")

totaal = 0

for snack in voorraad:
    print("-", snack, ":", voorraad[snack])
    totaal = totaal + voorraad[snack]

print("In totaal heeft de snackbar", totaal, "snacks.")