fd = open("cool.txt","w")

while True:
    print("Welkom bij mijn programma!!")
    keuze1 = input("wat is je naam? ")
    if keuze1 == "stop":
        fd.close()
        break
    fd.write(keuze1)
    fd.write(": ")
    print("De keuzes zijn: ")
    print("Hond en kat")
    keuze2 = input("Wat is je keuze? ")
    fd.write(keuze2 + "\n")