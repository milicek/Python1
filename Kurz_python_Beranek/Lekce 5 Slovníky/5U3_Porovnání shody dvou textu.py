import bs4
import urllib.request
#pip install bs4

odkaz1 = "http://zakony-online.cz/?s5&q5=all"
odkaz2 = "https://cs.wikipedia.org/wiki/Python"
text1 = """Vytvořte slovník, který obsahuje jako klíč jméno hráče a jako hodnotu jeho získáne skóre v nějaké pomyslné hře. 
Následně vypište na obrazovku tento slovník seřazený od nejlepšího do nejhoršího hráče. Také zkuste vypsat jen 5 nejlepších hráčů.
 Nápověda: až budete googlit, tak možná narazíte na import collections, pak víte, že jste na správné cestě."""
text1 = text1.lower().replace(","," ").replace("."," ").replace(":"," ").replace(";"," ").replace('"', ' ').replace("=", " ").replace("-"," ").strip()
"""webova_stranka1 = str(urllib.request.urlopen(odkaz1).read().decode('utf-8'))
text1 = bs4.BeautifulSoup(webova_stranka1).get_text()
#slova1 = set(text1.split())"""
cetnost_slov1 = {}
for slovo in text1.split():
    if slovo in cetnost_slov1.keys():
        cetnost_slov1[slovo] += 1
    else:
        cetnost_slov1[slovo] =  1



#print (cetnost_slov1)
text2 = """Dokončete program z online lekce, který zašifroval text pomocí substituční šifry (jedno písmenko nahradí za jiné). 
Udělejte v něm následující změny:
Aktuálně se může jedno písmenko přiřadit za jiné opakovaně. Např.: a->b, ale také h->b. Neexistuji tedy jednoznačné přiřazení.
Opravte program tak, aby se přiřazení neopakovalo, tzn dá se text jednoznačně rozluštit zpátky.
Upravte program tak, aby se postaral i o znaky v textu, které se nenachází ve slovníku (např. tečky, mezery, čárky, případně písmenka s háčkama a čárkama).
Zkuste následně zašifrovanou větu zpětně rozluštit do původního stavu podle slovníku vytvořte"""
text2 = text2.lower().replace(","," ").replace("."," ").replace(":"," ").replace(";"," ").replace('"', ' ').replace("=", " ").replace("-"," ").strip()
"""webova_stranka2 = str(urllib.request.urlopen(odkaz2).read().decode('utf-8'))
text2 = bs4.BeautifulSoup(webova_stranka2).get_text().lower()
#slova2 = set(text2.split())"""
cetnost_slov2 = {}
for slovo in text2.split():
    if slovo in cetnost_slov2.keys():
        cetnost_slov2[slovo] += 1
    else:
        cetnost_slov2[slovo] =  1

#print (cetnost_slov2)
v_obou = {}
for slovo, pocet in cetnost_slov1.items():
    if slovo in (cetnost_slov1.keys() and cetnost_slov2.keys()):
        v_obou[slovo] = [pocet, cetnost_slov2[slovo]]
        #print (slovo)
for slovo in v_obou:
  if v_obou[slovo][0] == v_obou[slovo][1]:
    print(f"{slovo} se v obou textech nachází {v_obou[slovo][0]} krát")



