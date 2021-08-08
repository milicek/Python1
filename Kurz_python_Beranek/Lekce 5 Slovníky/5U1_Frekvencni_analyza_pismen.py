text = input("Zadej text k analýze: ")

text = text.lower().replace(",","").replace(".","").replace(" ","").strip()

cetnost_pismen = {}
for pismeno in text:
    if pismeno in cetnost_pismen.keys():
        cetnost_pismen[pismeno] += 1
    else:
        cetnost_pismen[pismeno] =  1
cetnost_pismen = dict(sorted(cetnost_pismen.items(), key=lambda x: x[1], reverse=True))

for pismeno, cetnost in cetnost_pismen.items():
    print(pismeno, cetnost * "*")
