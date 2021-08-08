def vstup(text):
    promenna = input(text)
    return promenna


def main():
    portfolio = {}
    pridat = vstup("Přeješ si přidat nového klienta? ")
    #print(pridat)
    #pridat = input("Přeješ si přidat nového klienta? ")
    while pridat.lower() == "ano":
        jmeno= vstup("Zadej jméno nového klienta: ").lower()
        if jmeno in portfolio.keys():
            print("Klient už je v databázi")
        else:
            portfolio[jmeno] = {"Jméno" : jmeno}
            portfolio[jmeno]["email"] = vstup("Zadej email nového klienta: ")
            portfolio[jmeno]["telefon"] = vstup("Zadej telefon nového klienta: ")
            dalsi_akcie = "ano"
            portfolio[jmeno]["akcie"] = {}
            while dalsi_akcie.lower() == "ano":
                akcie, pocet = input("Zadejte název akcií a počet oddělený čárkou").split(",")
                portfolio[jmeno]["akcie"][akcie] = pocet
                dalsi_akcie = input("Přeješ si přidat další akcie? ")
        pridat = input("Přeješ si přidat dalšího klienta? ")
    for klient in portfolio:
        print(klient)
        for legenda, udaje in portfolio[klient].items():
            if legenda == "akcie":
                print(f"{legenda} :")
                for akcie, pocet in portfolio[klient][legenda].items():
                    print(f"{akcie} : {pocet}")
            else:
                print(f"{legenda} : {udaje}")



if __name__ == "__main__":
    main()
