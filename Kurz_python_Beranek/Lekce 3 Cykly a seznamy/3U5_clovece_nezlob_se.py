import random

delka = int(input("Jaká bude délka člověče nezlob se? "))
vypis = list("O" * delka)
hraci = int(input("Kolik bude hrát hráčů? "))

domecek = []
for i in range(hraci):
    radek = []
    for j in range(4):
        radek.append("*")
    domecek.append(radek)
cil = []
for i in range(hraci):
    radek = []
    for j in range(4):
        radek.append("")
    cil.append(radek)
pozice = []
for i in range(hraci):
    radek = []
    for j in range(4):
        radek.append("0")
    pozice.append(radek)

soucet = 0

while soucet != delka * 4:
    for i in range(hraci):
        print(f"Háže hráč číslo {i + 1}")
        input()
        hod = int(random.randint(1, 6))
        print(f"Hodil jsi {hod}")
        v_domku = domecek[i].count("*")
        v_cili = cil[i].count("*")
        if hod == 6:
            if 4 > v_domku > 0:
                nova = input("přeješ si nasadit novou figurku? a/n ")
                if nova == "a":
                    nasledujici = domecek[i].index("*")
                    pozice[i][nasledujici] = "1"
                    domecek[i][nasledujici] = " "
            elif v_domku == 4:
                print("Gratuluji. Můžeš vyrazit svou první figurkou.")
                pozice[i][0] = "1"
                domecek[i][-v_domku] = " "
        if v_domku + v_cili < 3:
            ktera = int(input("Kterou figurkou potáhneš? "))
            if int(pozice[i][ktera - 1]) + hod > delka:
                print("Touto figurkou nemůžeš táhnout, do domečklu zbývá menší počet políček než jsi hodil, za trest hází další hráč")
            else:
                int(pozice[i][ktera - 1]) += hod
                vypis[pozice[i][ktera - 1]] = pozice[i][ktera - 1]
        for j in range(4):
            if int(pozice[i][j]) > 0 and domecek[i][j] != "*" and cil[i][j] != "*":
                if pozice[i][j] + hod > delka:
                    print("Touto figurkou nemůžeš táhnout, do domečklu zbývá menší počet políček než jsi hodil, za trest hází další hráč")
                else:
                    pozice[i][j] += hod
                if pozice[i][j] == delka:
                    cil[i][j] = "*"
                else:
                    vypis[pozice[i][j]] = pozice[i][j]
        soucet = 0
        for k in range(4):
            soucet += pozice[i][k]
        if soucet == delka * 4:
            print(f"Gratuluji vyhrál hráč číslo {i}")
        for iradek in range(len(domecek)):
            print(domecek[iradek])
        print(vypis)

for iradek in range(len(domecek)):
    print(domecek[iradek])

print(vypis)