import model

nova_igra = model.Igra(stevilo_ladjic=4, ladjice=[3,4,4,5])

# postavljanje ladic
for igralec in range(1,3):
    print('Na vrsti je igralec' + int(igralec))
    for i in : ##
        try:
            postavitev = int(input("(0) je horizontalno 1 pa vertikalno"))
        except:
            print("neumen si")
        stolpec = int(input("Stolpec"))
        vrstica ##
        nova_igra.postavi(postavitev, stolpec, vrstica, i, igralec - 1)  ##

    
# igraš igro
na_vrsti = 0
while True:
    ## izpisi zgodovino strelov od igralca
    ## izpisi svoje polje
    print("na vrsti je ") ##
            stolpec = int(input("Stolpec, na katerega želite nardit genocid"))
        vrstica ##
    poteza = nova_igra.poteza(na_vrsti, stolpec, vrstica)
    if poteza == 'zmaga':
        print()##
    na_vrsti = not na_vrsti

#izpišeš zmagovalca