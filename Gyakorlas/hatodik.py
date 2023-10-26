def hat():
    szam = int(input("Kérem adjon meg egy valós számot!"))
    while not ( (szam % 3 == 0) or (szam ** 0.5 == int(szam ** 0.5))):
        print(szam)
        szam = int(input("Kérem adjon meg egy valós számot!"))
    print("A szám megfelelő!")
hat()