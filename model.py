class Igra(): 
    '''
    Polje : [polje[0],polje[1]],
     polje[i]: igralna plošča i-tega igralca
     polje[i][vrstica][stolpec] == -1: na mestu [vrstica][stolpec] ni nobene ladjice
     polje[i][vrstica][stolpec] == n: na mestu [vrstica][stolpec] je ladjica z indeksom n (to je indeks v seznamu ladjice)
     polje[i][vrstica][stolpec] == -2: mesto [vrstica][stolpec] je v neposredni bližini neke ladjice in zato ni prosto.
     primer seznama: ladjice = [2,4,4,5]

     zgodovina_strelov[i]: plošča kamor si i-ti igralec označuje uspele in neuspele strele
     zgodovina_strelov[i][vrstica][stolpec] = 0: zgrešena
     zgodovina_strelov[i][vrstica][stolpec] = 1: zadeta
    '''
    def __init__(self, st_nepotopljenih, ladjice): 
        self.polje = [[[-1] * 10 for i in range(10)], [[-1] * 10 for i in range(10)]]
        self.zgodovina_strelov = [[[-1] * 10 for i in range(10)], [[-1] * 10 for i in range(10)]]
        self.st_nepotopljenih = [st_nepotopljenih] * 2
        self.ladjice = [ladjice] * 2
    
    def ladje(self, igralec: bool):
        return self.ladjice[igralec]

    def zgodovina(self, igralec: bool):
        return self.zgodovina_strelov[igralec]

    def postavi(self, postavitev, vrstica, stolpec, indeks, na_vrsti): 
        '''
        Funkcija postavi ladjico v polje tako da z indeksom ladjice označi mesta v polju, kjer ladjica stoji.
        '''
        if vrstica in range(0, 10) and stolpec in range(0, 10):
            if self.polje[na_vrsti][vrstica][stolpec] != -1:
                return 'to mesto ni prosto'
            # Postavimo vodoravne ladjice:
            if postavitev == 0 and stolpec + self.ladjice[na_vrsti][indeks] <= 10:
                for i in range(stolpec, stolpec + self.ladjice[na_vrsti][indeks]):  # Postavi ladjico.
                    self.polje[na_vrsti][vrstica][i] = indeks
                if stolpec - 1 in range(0, 10):  # Označi mesto levo od ladjice.
                    self.polje[na_vrsti][vrstica][stolpec - 1] = -2
                if stolpec + self.ladjice[na_vrsti][indeks] in range(0, 10):  # Označi mesto desno od ladjice.
                    self.polje[na_vrsti][vrstica][stolpec + self.ladjice[na_vrsti][indeks]] = -2
                for i in range(stolpec, stolpec + self.ladjice[na_vrsti][indeks]):
                    if vrstica - 1 in range(0, 10):
                        self.polje[na_vrsti][vrstica - 1][i] = -2  # Označi mesta nad ladjico.
                        if stolpec - 1 in range(0, 10):  # Označi mesto levo zgoraj.
                            self.polje[na_vrsti][vrstica - 1][stolpec - 1] = -2
                        if stolpec + self.ladjice[na_vrsti][indeks] in range(0, 10):  # Označi mesto desno zgoraj.
                            self.polje[na_vrsti][vrstica - 1][stolpec + self.ladjice[na_vrsti][indeks]] = -2
                    if vrstica + 1 in range(0, 10):
                        self.polje[na_vrsti][vrstica + 1][i] = -2  # Označi mesta pod ladjico.
                        if stolpec - 1 in range(0, 10):  # Označi mesto levo spodaj.
                            self.polje[na_vrsti][vrstica + 1][stolpec - 1] = -2
                        if stolpec + self.ladjice[na_vrsti][indeks] in range(0, 10):  # Označi mesto desno spodaj.
                            self.polje[na_vrsti][vrstica + 1][stolpec + self.ladjice[na_vrsti][indeks]] = -2
                return True
            # Postavimo navpične ladjice: 
            elif postavitev == 1 and vrstica + self.ladjice[na_vrsti][indeks] <= 10: 
                for i in range(vrstica, vrstica + self.ladjice[na_vrsti][indeks]):  # Postavi ladjico.
                    self.polje[na_vrsti][i][stolpec] = indeks
                if vrstica - 1 in range(0, 10):  # Označi mesto nad ladjico.
                    self.polje[na_vrsti][vrstica - 1][stolpec] = -2
                if vrstica + self.ladjice[na_vrsti][indeks] in range(0, 10):  # Označi mesto pod ladjico.
                    self.polje[na_vrsti][vrstica + self.ladjice[na_vrsti][indeks]][stolpec] = -2
                for i in range(vrstica, vrstica + self.ladjice[na_vrsti][indeks]):
                    if stolpec - 1 in range(0, 10):
                        self.polje[na_vrsti][i][stolpec - 1] = -2  # Označi mesta levo od ladjice.
                        if vrstica - 1 in range(0, 10):  # Označi mesto levo zgoraj. 
                            self.polje[na_vrsti][vrstica - 1][stolpec - 1] = -2
                        if vrstica + self.ladjice[na_vrsti][indeks] in range(0, 10):  # Označi mesto levo spodaj. 
                            self.polje[na_vrsti][vrstica + self.ladjice[na_vrsti][indeks]][stolpec - 1] = -2
                    if stolpec + 1 in range(0, 10):
                        self.polje[na_vrsti][i][stolpec + 1] = -2  # Označi mesta desno od ladjice. 
                        if vrstica - 1 in range(0, 10):  # Označi mesto desno zgoraj. 
                            self.polje[na_vrsti][vrstica - 1][stolpec + 1] = -2  
                        if vrstica + self.ladjice[na_vrsti][indeks] in range(0, 10):  # Označi mesto desno zgoraj.
                            self.polje[na_vrsti][vrstica + self.ladjice[na_vrsti][indeks]][stolpec + 1] = -2   
                return True
        return False

    def poteza(self, na_vrsti, vrstica, stolpec): 
        '''
        Funkcija zabeleži potezo igralca in pove kako je poteza vplivala na igro. 
        '''
        if self.zgodovina_strelov[na_vrsti][vrstica][stolpec] != -1: 
            return 'napačen strel'
        if self.polje[na_vrsti][vrstica][stolpec] > -1:
            zadeta = self.polje[na_vrsti][vrstica][stolpec]
            self.ladjice[na_vrsti][zadeta] -= 1
            self.zgodovina_strelov[na_vrsti][vrstica][stolpec] = 1
            # Preverimo in shranimo, če je zadeta ladjica potopljena. 
            if self.ladjice[na_vrsti][zadeta] == 0: 
                self.st_nepotopljenih[na_vrsti] -= 1
                # tuki lahko dodam še iste pogoje kot zgoraj da zabeleži polja okoli potopljene ladjice
                # Preverimo ali smo potopili že vse.
                if self.st_nepotopljenih[na_vrsti] == 0: 
                    return 'zmaga'
                return 'potopljena'
            return 'zadeta'
        else:
            self.zgodovina_strelov[na_vrsti][vrstica][stolpec] = 0 
            return 'zgrešena'