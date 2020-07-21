import model

nova_igra = model.Igra(st_nepotopljenih=4, ladjice=[2,3,3,4])

# Postavljanje ladjic. 
# na_vrsti + 1 = igralec
for igralec in range(1,3):
    print("Na vrsti je igralec {}.".format(igralec))
    for indeks in range(0, len(nova_igra.ladje(igralec - 1)) -1):
        try:
            postavitev = int(input("Vnesi 0 za vodoravno ladjico in 1 za navpično:"))
        except:
            print("Poskusi ponovno postaviti.")
        vrstica = int(input("Vnesi številko vrstice:"))
        stolpec = int(input("Vnesi številko stolpca:"))
        nova_igra.postavi(postavitev, vrstica, stolpec, indeks, igralec - 1)

# Igranje igre. 
na_vrsti = 0
while True:
    print("Na vrsti je igralec {}".format(na_vrsti + 1))
    print("Polje igralca {}:".format(na_vrsti + 1))
    print(nova_igra.polje[na_vrsti])
    print("Zgodovina strelov igralca {}:".format(na_vrsti + 1))
    print(nova_igra.zgodovina_strelov[not na_vrsti])
    vrstica = int(input("Vrstica, kamor želiš streljati:"))
    stolpec = int(input("Stolpec, kamor želiš streljati:"))
    poteza = nova_igra.poteza(not na_vrsti, vrstica, stolpec)
    ## PREVERI OD TUKAJ NAPREJ
    if poteza == 'zmaga':
        print("Konec igre! Igralec {} je zmagovalec.".format(na_vrsti + 1))
    elif poteza == 'potopljena':
        print("Ladjica potopljena!")
    elif poteza == 'zadeta':
        print("Ladjica zadeta!")
    else:
        poteza == 'zgrešena'
        print("Strel v prazno.")
    na_vrsti = not na_vrsti

    #ZAKAJ NE IZPIŠE ZMAGE ČEPRAV JE ŽE KONEC IGRE?