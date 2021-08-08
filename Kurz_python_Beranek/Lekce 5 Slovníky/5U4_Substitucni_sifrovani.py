import string
import random

veta = input("Zadej vetu: ")
abeceda = list(string.ascii_lowercase)
pracovni_abeceda = list(string.ascii_lowercase)
substitucni_slovnik = {}

for pismenko in abeceda:
    nahodne_pismenko = random.choice(pracovni_abeceda)
    substitucni_slovnik[pismenko] = nahodne_pismenko
    pracovni_abeceda.remove(nahodne_pismenko)

zasifrovana_veta = ""
for pismenko in veta:
    if pismenko in substitucni_slovnik:
        zasifrovana_veta += substitucni_slovnik[pismenko]
    else:
        zasifrovana_veta += pismenko

print(zasifrovana_veta)
#print(substitucni_slovnik)
input("zmáčkni enter pro rozkodování")
rozsifrovana_veta = ""
for pismenko in zasifrovana_veta:
    for original, sifra in substitucni_slovnik.items():
        if pismenko in substitucni_slovnik:
            if pismenko in sifra:
                rozsifrovana_veta += original
                break
        else:
            rozsifrovana_veta += pismenko
            break

print(rozsifrovana_veta)