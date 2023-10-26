def negy():
    szam = int(input("Kérem adjon meg egy valós számot!"))

    if szam > 9 and szam % 2 == 0 and szam < 100:
        print(szam)
    else:
        print("A szám nem kétjegyű és páros szám")
negy()