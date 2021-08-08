hraci = {
    "Franta": 125,
    "Jarda": 74,
    "Jirka": 148,
    "Vilem": 127,
    "Jitka": 48,
    "Jana": 274,
    "Adela": 103,
    "Leona": 112,
    "Lucka": 38
}
serazeni_hraci = dict(sorted(hraci.items(), key= lambda x:x[1], reverse= True))
pocitadlo = 5
for hrac, skore in serazeni_hraci.items():
    if pocitadlo != 0:
        print(hrac, skore)
        pocitadlo -=1
