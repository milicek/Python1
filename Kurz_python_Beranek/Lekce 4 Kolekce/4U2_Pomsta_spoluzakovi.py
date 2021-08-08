import random

studenti = ["Abelesová", "Babiš", "Beránek", "Blatný", "Klomínek", "Martínek", "Novotná", "Prymula", "Zeman"]
fyzika = [1, 4, 4, 2, 3, 1, 2, 4, 5]
matematika = [2, 1, 5, 2, 4, 1, 2, 5, 4]
cestina = [4, 5, 4, 1, 2, 1, 3, 2, 4]
dejepis = [3, 3, 2, 4, 3, 1, 2, 2, 1]
vytvarka = [1, 2, 5, 4, 3, 1, 1, 4, 3]

#misto pro vas kod
poradi = studenti.index("Martínek")
if fyzika[poradi] < 5:
    fyzika[poradi] += random.randint(1,2)
if matematika[poradi] < 5:
    matematika[poradi] += random.randint(1,2)
if cestina[poradi] < 5:
    cestina[poradi] += random.randint(1,2)
if dejepis[poradi] < 5:
    dejepis[poradi] += random.randint(1, 2)
if vytvarka[poradi] < 5:
    vytvarka[poradi] += random.randint(1,2)

print(f"{studenti[poradi]}\n fyzika: {fyzika[poradi]}\n matematika: {matematika[poradi]}\n cestina: {cestina[poradi]}\n dejepis: {dejepis[poradi]}\n vytvarka: {vytvarka[poradi]}")
