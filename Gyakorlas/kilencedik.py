def kilenc():
    szoveg = input("Kérem írjon be egy szót: ")

    while not len(szoveg) == 4:
        print("A szónak pontosan 4 karakter hosszúnak kell lennie,próbálja újra!")
        szoveg = input("Kérem írjon be egy szót: ")

    print(szoveg.upper())
kilenc()