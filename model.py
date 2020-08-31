class Igra():
    '''
    Polje : [polje[0],polje[1]],
     polje[i]: igralna plošča i-tega igralca
     polje[i][vrstica][stolpec] == -1: na mestu [vrstica][stolpec] ni nobene ladjice
     polje[i][vrstica][stolpec] == n: na mestu [vrstica][stolpec] je ladjica z indeksom n (to je indeks v seznamu ladjice)
     polje[i][vrstica][stolpec] == -2: mesto [vrstica][stolpec] je v neposredni bližini neke ladjice in zato ni prosto.
     primer seznama: ladjice = [2,4,4,5]

     zgodovina_strelov[i]: plošča kamor si i-ti igralec označuje uspele in neuspele strele
     zgodovina_strelov[i][vrstica][stolpec] = -1: sem še nismo ciljali
     zgodovina_strelov[i][vrstica][stolpec] = 0: zgrešena
     zgodovina_strelov[i][vrstica][stolpec] = 1: zadeta
    '''

    def __init__(self, ladjice):
        self.polje = [
            [[-1] * 10 for i in range(10)], [[-1] * 10 for i in range(10)]]
        self.zgodovina_strelov = [
            [[-1] * 10 for i in range(10)], [[-1] * 10 for i in range(10)]]
        self.st_nepotopljenih = [len(ladjice), len(ladjice)]
        # Med igro služi kot življenjske točke ladjice, prej pa kot dolžina ladjice.
        self.ladjice = [ladjice[:], ladjice[:]]
        

    def ladje(self, igralec: bool):
        return self.ladjice[igralec]

    def zgodovina(self, igralec: bool):
        return self.zgodovina_strelov[igralec]

    def postavi(self, postavitev, vrstica, stolpec, indeks, na_vrsti):
        '''
        Funkcija postavi ladjico v polje tako da z indeksom ladjice označi mesta v polju, kjer ladjica stoji.
        '''
        if vrstica in range(0, 10) and stolpec in range(0, 10):
            # Preverimo, da polja kjer bo ladjica še niso zasedena:
            kaj_zasede = zip([vrstica + j for j in range(self.ladjice[na_vrsti][indeks])], [stolpec] * 10)
            if not postavitev:             
                kaj_zasede = zip([vrstica] * 10, [stolpec + j for j in range(self.ladjice[na_vrsti][indeks])])
            for st_vrstice, st_stolpca in kaj_zasede:
                if self.polje[na_vrsti][st_vrstice][st_stolpca] != -1:
                    return False

            # Postavimo vodoravne ladjice:
            if postavitev == 0 and stolpec + self.ladjice[na_vrsti][indeks] <= 10:
                # Postavi ladjico.
                for i in range(stolpec, stolpec + self.ladjice[na_vrsti][indeks]):
                    self.polje[na_vrsti][vrstica][i] = indeks
                # Označi mesto levo od ladjice.
                if stolpec - 1 in range(0, 10):
                    self.polje[na_vrsti][vrstica][stolpec - 1] = -2
                # Označi mesto desno od ladjice.
                if stolpec + self.ladjice[na_vrsti][indeks] in range(0, 10):
                    self.polje[na_vrsti][vrstica][stolpec +
                                                  self.ladjice[na_vrsti][indeks]] = -2
                for i in range(stolpec, stolpec + self.ladjice[na_vrsti][indeks]):
                    if vrstica - 1 in range(0, 10):
                        # Označi mesta nad ladjico.
                        self.polje[na_vrsti][vrstica - 1][i] = -2
                        # Označi mesto levo zgoraj.
                        if stolpec - 1 in range(0, 10):
                            self.polje[na_vrsti][vrstica - 1][stolpec - 1] = -2
                        # Označi mesto desno zgoraj.
                        if stolpec + self.ladjice[na_vrsti][indeks] in range(0, 10):
                            self.polje[na_vrsti][vrstica - 1][stolpec +
                                                              self.ladjice[na_vrsti][indeks]] = -2
                    if vrstica + 1 in range(0, 10):
                        # Označi mesta pod ladjico.
                        self.polje[na_vrsti][vrstica + 1][i] = -2
                        # Označi mesto levo spodaj.
                        if stolpec - 1 in range(0, 10):
                            self.polje[na_vrsti][vrstica + 1][stolpec - 1] = -2
                        # Označi mesto desno spodaj.
                        if stolpec + self.ladjice[na_vrsti][indeks] in range(0, 10):
                            self.polje[na_vrsti][vrstica + 1][stolpec +
                                                              self.ladjice[na_vrsti][indeks]] = -2
                return True
            # Postavimo navpične ladjice:
            elif postavitev == 1 and vrstica + self.ladjice[na_vrsti][indeks] <= 10:
                # Postavi ladjico.
                for i in range(vrstica, vrstica + self.ladjice[na_vrsti][indeks]):
                    self.polje[na_vrsti][i][stolpec] = indeks
                if vrstica - 1 in range(0, 10):  # Označi mesto nad ladjico.
                    self.polje[na_vrsti][vrstica - 1][stolpec] = -2
                # Označi mesto pod ladjico.
                if vrstica + self.ladjice[na_vrsti][indeks] in range(0, 10):
                    self.polje[na_vrsti][vrstica +
                                         self.ladjice[na_vrsti][indeks]][stolpec] = -2
                for i in range(vrstica, vrstica + self.ladjice[na_vrsti][indeks]):
                    if stolpec - 1 in range(0, 10):
                        # Označi mesta levo od ladjice.
                        self.polje[na_vrsti][i][stolpec - 1] = -2
                        # Označi mesto levo zgoraj.
                        if vrstica - 1 in range(0, 10):
                            self.polje[na_vrsti][vrstica - 1][stolpec - 1] = -2
                        # Označi mesto levo spodaj.
                        if vrstica + self.ladjice[na_vrsti][indeks] in range(0, 10):
                            self.polje[na_vrsti][vrstica +
                                                 self.ladjice[na_vrsti][indeks]][stolpec - 1] = -2
                    if stolpec + 1 in range(0, 10):
                        # Označi mesta desno od ladjice.
                        self.polje[na_vrsti][i][stolpec + 1] = -2
                        # Označi mesto desno zgoraj.
                        if vrstica - 1 in range(0, 10):
                            self.polje[na_vrsti][vrstica - 1][stolpec + 1] = -2
                        # Označi mesto desno zgoraj.
                        if vrstica + self.ladjice[na_vrsti][indeks] in range(0, 10):
                            self.polje[na_vrsti][vrstica +
                                                 self.ladjice[na_vrsti][indeks]][stolpec + 1] = -2
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
                # Preverimo ali smo potopili že vse.
                if self.st_nepotopljenih[na_vrsti] == 0:
                    return 'zmaga'
                return 'potopljena'
            return 'zadeta'
        else:
            self.zgodovina_strelov[na_vrsti][vrstica][stolpec] = 0
            return 'zgrešena'

class Streznik:
    def __init__(self):
        self.igre = {}  
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self, ladjice):
        id = self.prost_id_igre()
        igra = Igra(ladjice)
        self.igre[id] = [igra]
        print(igra)
        return id