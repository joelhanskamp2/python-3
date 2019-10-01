input_Keuze = ""
keuzes = {"appel": 1.8, "paprika chips": 1.2, "aa drink": 1.1, "laptop": 1099.0}
totaalprijs = 0
keuze1 = input("Hallo, Welkom in de winkel, Wat is je naam: ")
keuze2 = ""

def boodschappen_Doen():
    print("U kunt deze dingen kopen:")
    print(keuzes)
    keuze2 = input("Wat wilt u kopen? ")
    if keuze2 in keuzes:
        ff = keuzes[keuze2]
        ff2 = str(ff)
        print("Dat kost dan: " + ff2)
        ff2 = float(ff)
        hoeveel_kg = float(input("hoeveel Kg/stuks wilt u? "))
        tijdelijk_Prijs = ff2*hoeveel_kg
        tijdelijk_Prijs = round(tijdelijk_Prijs, 2)
        tijdelijk_Prijs = str(tijdelijk_Prijs)
        print("totaal van dit product:" + tijdelijk_Prijs)
        tijdelijk_Prijs = float(tijdelijk_Prijs)
        totaalprijs = float(0)
        totaalprijs += tijdelijk_Prijs
        totaalprijs = str(totaalprijs)
        print("Dit is je totaalprijs: " + totaalprijs)
        totaalprijs = float(totaalprijs)

def seeProducten():
    print("Dit zijn de dingen die wij verkopen")
    print(keuzes)

def plusProduct():
    gg = input("welk product wil je toevoegen? ")
    gg2 = input("welke prijs heeft dat product? ")
    keuzes[gg] = gg2
    print(keuzes)

def changeProduct():
    zz = input("welk product wil je veranderen? ")
    zz2 = input("wat moet de nieuwe prijs worden? ")
    if zz in keuzes:
        del keuzes[zz]
        keuzes[zz] = zz2

def delProduct():
    kk = input("welk product wilt u verwijderen? ")
    if kk in keuzes:
        del keuzes[kk]

def zieProducten():
    print(keuzes)

while (input_Keuze != "stop"):
    print("toets 1 om alle producten te bekijken.")
    print("toets 2 om een product toe te voegen.")
    print("toets 3 om een product of diens prijs aan te passen.")
    print("toets 4 om een product en diens prijs te verwijderen")
    print("toets 5 om boodschappen te doen")
    print("toets 6 om de lijst van producten te zien.")
    input_Keuze = int(input("uw keuze: "))
    if input_Keuze == 1:
        seeProducten()
    if input_Keuze == 2:
        plusProduct()
    if input_Keuze == 3:
        changeProduct()
    if input_Keuze == 4:
        delProduct()
    if input_Keuze == 5:
        boodschappen_Doen()
    if input_Keuze == 6:
        zieProducten()