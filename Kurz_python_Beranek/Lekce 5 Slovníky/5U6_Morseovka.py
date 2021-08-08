legenda = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
           "k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
           "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
text = input("Zadej text který chceš přenést do morseovky : ")
morseovka = ""
for pismeno in text:
    if pismeno.lower() in legenda.keys():
        morseovka += legenda[pismeno.lower()] + " "
    else:
        morseovka += pismeno.lower() + " "
print(morseovka)