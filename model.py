class Igra(): 
    '''
    Polje : [polje[0],polje[1]],
     polje[i]: igralna plošča itega igralca
     polje[i][vrstica][stolpec] == -1: na mestu [vrstica][stolpec] ni nobene ladice
     polje[i][v][s] == n: namestu v,s je ladica z indeksom n (to je indeks v tabeli ladice)

     [2,4,4,5]
    '''
    def __init__(self, st_nepotopljenih, ladjice): 
        self.polje = [[[-1] * 10 for i in range(10)], [[-1] * 10 for i in range(10)]]]
        self.zgodovina_strelov = [[[0] * 10] * 10, [[0] * 10] * 10]
        self.st_nepotopljenih = [st_nepotopljenih] * 2
        self.ladjice = [ladjice] * 2

    def postavi(self, postavitev, vrstica, stolpec, indeks, na_vrsti): 
        if vrstica in range(0, 10) and stolpec in range(0,10):
            # Ali je postavitev pravilna, če je ladjica vodoravna.
            if postavitev == 0 and stolpec + self.ladjice[na_vrsti][indeks] <= 10: 
                for i in range(stolpec, stolpec + self.ladjice[na_vrsti][indeks]): 
                    self.polje[na_vrsti][vrstica][i] = indeks
                return True
        return False

    def poteza(self, na_vrsti, vrstica, stolpec): 
        if polje[na_vrsti][vrstica][stolpec] > -1:
            zadeta = polje[na_vrsti][vrstica][stolpec]  #katero smo zadeli
            ladjice[zadeta] -= 1  #zabeležimo zadetek
            # Preverimo ali je zadeta ladjica potopljena. 
            if ladjice[zadeta] == 0: 
                st_nepotopljenih -= 1
                # Preverimo ali smo potopili že vse
                if st_nepotopljenih == 0: 
                    return 'zmaga'
                return 'potopljena'
            return 'zgrešena'