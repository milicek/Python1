zadani = input("Zadejte pole pro analyzu, řádky oddělte čárkami").split(",")
mapka = []
for radek in zadani:
    rada_symbolu = []
    for symbol in radek:
        rada_symbolu.append(symbol)
    mapka.append(rada_symbolu)

for radek in mapka:
    print(radek)

for hrac in ["o","x"]:
    for radek in mapka:
        if all(symbol == hrac for symbol in radek):
            vitez = hrac
            break
    for isloupec in range(len(mapka)):
        sloupec = (radek[isloupec] for radek in mapka)
        if all(symbol == hrac for symbol in sloupec):
            vitez = hrac
            break
    diagonala1 = [mapka[i][i] for i in range(len(mapka))]
    diagonala2 = [mapka[i][-(i+1)] for i in range(len(mapka))]
    #print(diagonala2)
    if all(symbol == hrac for symbol in diagonala1) or all(symbol == hrac for symbol in diagonala2):
        vitez = hrac
    else:
        vitez = "nikdo"

if vitez != "nikdo":
    print(f"vítězem je hráč {vitez}")
else:
    print("Tyto piškvorky nemají vítěze")