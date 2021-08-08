import string


def input_integer(text, error):
    pocet = input(text)
    while type(pocet) != int:
        try:
            pocet = int(pocet)
        except:
            print(error)
            pocet = input(text)
    return pocet


def make_pole(cislo):
    pole = []
    for i in range(cislo):
        radek = []
        for j in range(cislo):
             radek.append("   ")
        pole.append(radek)
    return pole


def zobraz_pole(pole):
    print(legenda(pole))
    print("|"+(len(pole)+1)* "---|")
    for radek in pole:
        test = ""
        for pismeno in radek:
            test += "|"
            test += pismeno
        test += "|"
        print(test)
        print("|"+(len(pole)+1)* "---|")


def legenda(pole):
    if pole[0][0] != " 1 ":
        cislo = 1
        for sloupec in pole:
            if cislo < 10:
                sloupec.insert(0, " "+str(cislo)+" ")
            elif 100 > cislo >= 10:
                sloupec.insert(0, " "+str(cislo))
            cislo += 1
    legenda = "|   |"
    for i in range(len(pole)):
        legenda += " " + string.ascii_uppercase[i] + " "
        legenda = legenda + "|"
    return legenda


def vyber_symbol():
    symbol = input("Vyber symbol s kterým budeš hrát: ")
    while len(symbol) > 1:
            print("Vyber si jen jeden znak")
            symbol = input("Vyber symbol s kterým budeš hrát")
    return symbol



def zapis_pozice(pole,souradnice,hrac):
    sloupec = string.ascii_lowercase.index(souradnice[0].lower())
    pole[(int(souradnice[1:]))-1][sloupec+1] = " " + hrac + " "



def tah(pole):
    while True:
        souradnice = str(input("Zadej souřadnice tvého tahu: "))
        if souradnice[0].lower() in string.ascii_lowercase[0:len(pole)]:
            try:
                radek = int(souradnice[1:])
                if radek > len(pole):
                    print("Zadal jsi větší číslo než je počet řádků")
                    continue
                else:
                    if pole[(int(souradnice[1:]))-1][(string.ascii_lowercase.index(souradnice[0].lower()))+1] != "   ":
                        print("Pole už je obsazené, musíš táhnout jinak")
                        continue
                    else:
                        break
            except:
                print("Druhá souřadnice není číslo")
                continue
        else:
            print(
                "Chybně zadané souřadnice.Prvně napiš písmeno a potom číslo, nebo jsi použil písmeno které není na hrací ploše")
            continue
    return souradnice



def vyhodnoceni_radek(pole):
    for radek in pole:
        for symbol in radek:
            if symbol != "   ":
                hrac = symbol
        if radek.count(hrac) >= 5:
            return hrac
        else:
            return ""


def vyhodnoceni_sloupec(pole):
    for radek in pole:
        for symbol in radek:
            if symbol != "   ":
                hrac = pole.index[radek][symbol]
                break
    for i in range(5):
        pass
    print("ahoj hhgdfsrfggg")


def main():
    hraci = input_integer("Zadej počet hráčů: ","Musíš zadat počet hráčů pomoci čísla ")
    seznam_hracu = []
    for hrac in range(hraci):
        print(f"Hráč číslo{hrac + 1}")
        symbol = vyber_symbol()
        seznam_hracu += symbol
    pole = make_pole(input_integer("Zadej velikost pole: ", "Musíš zadat jedno číslo"))
    print(pole)
    zobraz_pole(pole)
    vitez = ""
    while len(vitez) < 1:
        for hrac in seznam_hracu:
            print(f"Hraje hráč se symbolem{hrac}")
            zapis_pozice(pole,tah(pole),hrac)
            vitez = vyhodnoceni_radek(pole)
        zobraz_pole(pole)




if __name__ == "__main__":
    main()