def harom():
    szam = int(input("Kérem adjon meg egy valós számot! "))

    if szam % 10 ==0:
        print(szam)
    else:
        print("A szám nem osztható 10-el!")

harom()