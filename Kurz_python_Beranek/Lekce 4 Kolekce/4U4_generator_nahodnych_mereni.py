import random

hodnoty = []
for i in range(100):
    hodnoty.append(random.randint(150,200))

#aritmetický průměr
soucet = 0
for hodnota in hodnoty:
    soucet += hodnota
prumer = soucet / len(hodnoty)
print(f"Aritmetický průměr naměřených hodnot je {prumer}")

#výpočet modusu
vysledek = [0,0]
pocet_opakovani = 0
for hodnota in hodnoty:
    if hodnoty.count(hodnota) > vysledek[1]:
        vysledek[0] = hodnota
        vysledek[1] = hodnoty.count(hodnota)
print (f"Modus je číslo {vysledek[0]} které se v hodnotách vyskytuje {vysledek[1]} krát")

hodnoty.sort()
median = (hodnoty[49] + hodnoty[50])/2
print(f"median je číslo {median}")
