#def soucet(a, b):
#    return 5

#def soucet(a, b):
#    if a == 2:
#        return 5
#    else:
#        return 7

def soucet(a, b):
    return a + b



def podil(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Dělení nulou")
        return None

def main():
    assert soucet(2,3) == 5, "Chyba v souctu"
    assert soucet(3,4) == 7, "Chyba v souctu"
    assert soucet(5,5) == 10, "Chyba v souctu"
    assert podil(3,3) == 1, "Chyba v podilu"
    assert podil(6,2) == 3, "Chyba v podilu"
    assert podil(7,2) == 3.5, "Chyba v podilu"
    assert podil(7,0) == None, "Chyba v podilu"



if __name__ == "__main__":
    main()