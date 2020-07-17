class Igra(): 
    def __init__(self, st_nepotopljenih, ladjice): 
        self.polje = [[[0] * 10] * 10, [[0] * 10] * 10]
        self.zgodovina_strelov = [[[0] * 10] * 10, [[0] * 10] * 10]
        self.st_nepotopljenih = [st_nepotopljenih] * 2
        self.ladjice = [ladjice] * 2

    def postavi(self, postavitev, vrstica, stolpec, dolzina): 
        if vrstica, stolpec in range(1, 11):
            # Ali je postavitev pravilna, če je ladjica vodoravna.
            if postavitev == 0 and int(self.polje[na_vrsti][vrstica][stolpec + dolzina]) in range(1, 11):
                self.polje[na_vrsti][vrstica][stolpec:stolpec + dolzina] = dolzina #nastavimo vsa mesta kjer je ladjica na številko ladjice
            elif postavitev == 1 and int(self.polje[na_vrsti][vrstica + dolzina][stolpec]) in range(1, 11):
                self.polje[na_vrsti][vrstica:vrstica + dolzina][stolpec] = dolzina
        else: 
            return 'napačno postavljena'

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