import bs4
import urllib.request
#pip install bs4

odkaz1 = "https://cs.wikipedia.org/wiki/Programov%C3%A1n%C3%AD"
odkaz2 = "https://cs.wikipedia.org/wiki/Python"

#zde dopište kód
webova_stranka1 = str(urllib.request.urlopen(odkaz1).read().decode('utf-8'))
text1 = bs4.BeautifulSoup(webova_stranka1).get_text()
slova1 = set(text1.split())
#print (slova1)
webova_stranka2 = str(urllib.request.urlopen(odkaz2).read().decode('utf-8'))
text2 = bs4.BeautifulSoup(webova_stranka2).get_text()
slova2 = set(text2.split())
print(slova2)

print("Tato slova obsahují oba dokumenty :")
print(slova1.intersection(slova2))

print("Tato slova jsou jedinečná pro první webovou stránku")
print(slova1.difference(slova2))

print("Tato slova jsou jedinečná pro druhou webovou stránku")
print(slova2.difference(slova1))


