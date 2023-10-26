def ot():
    szam = int(input("Kérem adjon meg egy valós számot!"))
    while not (szam > 0 and szam % 2 == 0):
            print(szam)
            szam = int(input("Kérem adjon meg egy valós számot!"))
    print("A szám nem megfelelő!")
ot()
