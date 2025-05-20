ukoly = []

def hlavni_menu():
    print(ukoly)
    select = int()
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        select = input("Vyberte možnost (1-4): ")
        print("")
        try:
            select = int(select)
        except:
            print("Chyba")
            quit()
        if not isinstance(select, int):
            print("Výběr musí být číslo")
        elif not select in range(1, 5):
            print("Vyběr musí být v rozsahu 1-4")
        else:
            if select == 4:
                print("Konec programu.")
                quit()
            if select == 1:
                pridat_ukol()
            if select == 2:
                zobrazit_ukoly()
            if select == 3:
                odstranit_ukol()


def pridat_ukol():
    loop = 1
    while loop == 1: 
        name = input("Zadejte název úkolu: ")
        description = input("Zadejte popis úkolu: ")

        if name != "" or description != "":
            loop = 0
        else:
            print("Název ani popis nesmí být prýzdný!")
    ukoly.append([name, description])
    print("")


    hlavni_menu()


def zobrazit_ukoly():
    print("Seznam úkolů: ")
    i = 1
    for ukol in ukoly:
        print(f"{i}. {ukol[0]} - {ukol[1]}")
        i += 1
    print("")


    hlavni_menu()


def odstranit_ukol():
    select = input("Zdaejte číslo úkolu, který chcete odstranit: ")
    try:
        select = int(select)
    except:
        print("Chyba")
        quit()
    try:
        ukoly.pop(select-1)
    except:
        print("Chyba")
    
print("")


        hlavni_menu()


def run():
    hlavni_menu()


if __name__ == "__main__":
    run()