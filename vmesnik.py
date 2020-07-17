import model
Vprašaj uporabnika, kam želi postavit ladjice. 
nova_igra = modul.Igra(stevilo_ladjic=10, ladice=[4, 3, 3, 2, 2, 2, 1, 1, 1, 1])

# postavljanje ladic
for i in ladjice:
    try:
        postavitev = int(input("(0) je horizontalno 1 pa vertikalno"))
    except:
        print("neumen si")
    stolpec = int(input("Stolpec"))
    vrstica
    nova_igra.postavi(postavitev, stolpec, vrstica, dolzina)
while True:
    modulu povedal, kam hoče igralec streljat
    