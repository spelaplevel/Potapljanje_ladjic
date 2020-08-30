import model

nova_igra = model.Igra(ladjice=[2,3])

# Postavljanje ladjic. 
# na_vrsti + 1 = igralec
for igralec in range(1, 3): 
    print("Na vrsti je igralec {}.".format(igralec))
    for indeks in range(len(nova_igra.ladje(igralec - 1))):
        postavitev = int(input("Vnesi 0 za vodoravno ladjico in 1 za navpično:"))
        vrstica = int(input("Vnesi številko vrstice:"))
        stolpec = int(input("Vnesi številko stolpca:"))
        postavitev = nova_igra.postavi(postavitev, vrstica, stolpec, indeks, igralec - 1)

# Igranje igre. 
na_vrsti = 0
while True:
    print("Na vrsti je igralec {}".format(na_vrsti + 1))
    print("Polje igralca {}:".format(na_vrsti + 1))
    polje = nova_igra.polje[na_vrsti]
    for vrstica in polje:
        print(vrstica)
    print('\n')
    
    print("Zgodovina strelov igralca {}:".format(na_vrsti + 1))
    for vrstica in nova_igra.zgodovina_strelov[not na_vrsti]:
        print(vrstica)

    vrstica = int(input("Vrstica, kamor želiš streljati:"))
    stolpec = int(input("Stolpec, kamor želiš streljati:"))
    poteza = nova_igra.poteza(not na_vrsti, vrstica, stolpec)

    if poteza == 'zmaga':
        print(f"Konec igre! Igralec {na_vrsti + 1} je zmagovalec.")
        break
    elif poteza == 'potopljena':
        print("Ladjica potopljena!")
    elif poteza == 'zadeta':
        print("Ladjica zadeta!")
    else:
        poteza == 'zgrešena'
        print("Strel v prazno.")
    na_vrsti = not na_vrsti