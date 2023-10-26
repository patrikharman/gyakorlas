def nyolc():
    szoveg = input("Kérem írjon be egy szót: ")

    while len(szoveg) < 3:
        print("A szónak legalaább 3 karakter hosszúnak kell lennie,próbálja újra!")
        szoveg = input("Kérem írjon be egy szót: ")

    print(szoveg.upper())
nyolc()
