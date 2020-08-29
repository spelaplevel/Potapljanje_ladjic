import model

nova_igra = model.Igra(ladjice=[2,3])

# Postavljanje ladjic. 
# na_vrsti + 1 = igralec
#for igralec in range(1, 3): 
#    print("Na vrsti je igralec {}.".format(igralec))
#    for indeks in range(len(nova_igra.ladje(igralec - 1))):
#        postavitev = int(input("Vnesi 0 za vodoravno ladjico in 1 za navpično:"))
#        vrstica = int(input("Vnesi številko vrstice:"))
#        stolpec = int(input("Vnesi številko stolpca:"))
#        postavitev = nova_igra.postavi(postavitev, vrstica, stolpec, indeks, igralec - 1)
nova_igra.postavi(0, 0, 0, 0, 0)
nova_igra.postavi(0, 5, 0, 1, 0)
nova_igra.postavi(1, 0, 0, 0, 1)
nova_igra.postavi(1, 0, 5, 1, 1)
# Igranje igre. 
na_vrsti = 0
while True:
    print("Na vrsti je igralec {}".format(na_vrsti + 1))
    polje = nova_igra.polje[na_vrsti]
    for vrstica in polje:
        print(vrstica)
    print('\n')
    #print("Polje igralca {}:".format(na_vrsti + 1))
   # print(nova_igra.polje[na_vrsti])
    print("Zgodovina strelov igralca {}:".format(na_vrsti + 1))

    for i in nova_igra.zgodovina_strelov[not na_vrsti]:
        print(i)
   # print(nova_igra.zgodovina_strelov[not na_vrsti])

    vrstica = int(input("Vrstica, kamor želiš streljati:"))
    stolpec = int(input("Stolpec, kamor želiš streljati:"))
    poteza = nova_igra.poteza(not na_vrsti, vrstica, stolpec)
    ## PREVERI OD TUKAJ NAPREJ
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

    #ZAKAJ NE IZPIŠE ZMAGE ČEPRAV JE ŽE KONEC IGRE?
