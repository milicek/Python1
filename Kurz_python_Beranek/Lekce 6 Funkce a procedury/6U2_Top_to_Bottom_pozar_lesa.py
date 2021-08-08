import random
import copy
import matplotlib.pyplot as plt

def vytvor_matici():
    x = int(input("Zadej počet řádků matice: "))
    y = int(input("Zadej počet sloupců matice: "))
    matice = []
    for i in range(x):
        radek = []
        for j in range(y):
            radek.append(0)
        matice.append(radek)
    return matice


def nahodne_zapal(matice):
    for i in range(random.randint(1, 10)):
        x = random.randint(0, (len(matice))-1)
        y = random.randint(0, (len(matice[0])-1))
        matice[x][y] = 1


def sireni_ohne(matice):
    matice_copy = copy.deepcopy(matice)
    for i, radek in enumerate(matice_copy):
        for j, bod in enumerate(radek):
            if bod > 0:
                zapal_sousedy(matice,i,j)


def zapal_sousedy(matice,i,j):
    for k in range(-1, 2):
        if i + k >= len(matice) or i + k < 0:
            continue
        for l in range(-1, 2):
            if j + l >= len(matice) or j + l < 0:
                continue
            matice[i + k][j + l] += 1



def draw_forest(forest):
    plt.imshow(forest, cmap='plasma')
    plt.show()




def main():
    matice = vytvor_matici()
    nahodne_zapal(matice)
    for i in range(10):
        sireni_ohne(matice)
    draw_forest(matice)








if __name__ == "__main__":
    main()