import random

pavel_filmy = [
               ("Vykoupení z věznice Shawshank", 10),
               ("Slunovrat", 7),
               ("Joker", 9),
               ("The Queen's gambit", 8),
               ("Likehouse", 1)
               ]
jaroslav_filmy = [
                  ("Mama ožen ma", 4),
                  ("Paranormal activity", 3),
                  ("Záhada Blair witch", 8),
                  ("Battle Royale", 8),
                  ("Resident evil", 4)
                  ]
alena_filmy = [
               ("Starwars episode 7", 8),
               ("Chata v horách", 7),
               ("Výměna manželek", 10),
               ("Ulice", 8),
               ("Mulan", 5)
               ]

#zde napište svůj kód
vse = pavel_filmy + jaroslav_filmy + alena_filmy
vse.sort(key=lambda x:x[1],reverse=True)
top5 = vse[:5]
print(vse[:5])
print(f"Dnes se můžete kouknout na film : {top5[(random.randint(1,5)-1)][0]}")