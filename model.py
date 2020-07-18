class Igra(): 
    '''
    Polje : [polje[0],polje[1]],
     polje[i]: igralna plošča i-tega igralca
     polje[i][vrstica][stolpec] == -1: na mestu [vrstica][stolpec] ni nobene ladjice
     polje[i][vrstica][stolpec] == n: na mestu [vrstica][stolpec] je ladjica z indeksom n (to je indeks v seznamu ladjice).

     ladjice = [2,4,4,5]
    '''
    def __init__(self, st_nepotopljenih, ladjice): 
        self.polje = [[[-1] * 10 for i in range(10)], [[-1] * 10 for i in range(10)]]
        self.zgodovina_strelov = [[[0] * 10 for i in range(10)], [[0] * 10 for i in range(10)]]
        self.st_nepotopljenih = [st_nepotopljenih] * 2
        self.ladjice = [ladjice] * 2

    def postavi(self, postavitev, vrstica, stolpec, indeks, na_vrsti): 
        '''
        Funkcija postavi ladjico v polje tako da z indeksom ladjice označi mesta v polju, kjer ladjica stoji.
        '''
        if vrstica in range(0, 10) and stolpec in range(0, 10):
            # Postavimo vodoravne ladjice:
            if postavitev == 0 and stolpec + self.ladjice[na_vrsti][indeks] <= 10: 
                for i in range(stolpec, stolpec + self.ladjice[na_vrsti][indeks]): 
                    self.polje[na_vrsti][vrstica][i] = indeks
                return True
            # Postavimo navpične ladjice: 
            elif postavitev == 1 and vrstica + self.ladjice[na_vrsti][indeks] <= 10: 
                for i in range(vrstica, vrstica + self.ladjice[na_vrsti][indeks]):
                    self.polje[na_vrsti][i][stolpec] = indeks
                return True
        return False

    def poteza(self, na_vrsti, vrstica, stolpec): 
        '''
        Funkcija zabeleži potezo igralca in pove kako je poteza vplivala na igro. 
        '''
        if self.polje[na_vrsti][vrstica][stolpec] > -1:
            zadeta = self.polje[na_vrsti][vrstica][stolpec]
            self.ladjice[na_vrsti][zadeta] -= 1
            #self.polje[na_vrsti][vrstica][stolpec] = -2 #v polju označim da je tukaj zadeta ladjica
            # Preverimo in shranimo, če je zadeta ladjica potopljena. 
            if self.ladjice[na_vrsti][zadeta] == 0: 
                self.st_nepotopljenih -= 1
                # Preverimo ali smo potopili že vse.
                if self.st_nepotopljenih == 0: 
                    return 'zmaga'
                return 'potopljena'
            return 'zadeta'
        else: 
            return 'zgrešena'