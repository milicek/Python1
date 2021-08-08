from PIL import Image

obrazek = Image.open("test.jpg")
sirka, vyska = obrazek.size

pixel = obrazek.getpixel((sirka-1,vyska-1))

maxpixel = (0,0,0)
souradnice_maxpixelu = (0,0)

for x in range(sirka):
    for y in range(vyska):
        if sum(obrazek.getpixel((x,y))) > sum(maxpixel):
            maxpixel = obrazek.getpixel((x,y))
            souradnice_maxpixelu = (x,y)
print(f"nejsvětlelší pixel má barvu {maxpixel} a je na pozici {souradnice_maxpixelu}")


c = souradnice_maxpixelu
for dx in range(-20, 20, 1):
    for dy in range(-20, 20, 1):
        obrazek.putpixel((c[0]+dx, c[1]+dy), (255, 0, 0))
obrazek.putpixel((c[0], c[1]), (0,255,0))

print(obrazek.show)


def main():



#grayscale
from statistics import mean

obrazek = Image.open("gjj.jpg")
sirka, vyska = obrazek.size

for x in range(sirka):
    for y in range(vyska):
        pixel = obrazek.getpixel((x,y))
        avg = int(mean(pixel))
        #vetší světlost avg = int((max(pixel) + min(pixel))/2
        obrazek.putpixel((x, y), (avg, avg, avg))

display(obrazek)


#binarizace
import random
from statistics import mean

obrazek = Image.open("gjj.jpg")
sirka, vyska = obrazek.size

for x in range(sirka):
    for y in range(vyska):
        pixel = obrazek.getpixel((x,y))
        avg = int(mean(pixel))
        if avg > 127:
            obrazek.putpixel((x, y), (255,255,255))
        else:
            obrazek.putpixel((x, y), (0,0,0))

display(obrazek)


#hledani v obrazku
!python -m pip install opencv-python



















































if __name__ == "__main__":
    main()









