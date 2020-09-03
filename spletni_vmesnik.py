import model
import bottle

streznik = model.Streznik()
SKRIVNOST = 'skrivnost'

standardne_ladje = [2,2,3]

# Povzeto po viru.
def id():
    try:
        id_piskotek = int(bottle.request.get_cookie('id_igre', secret=SKRIVNOST))
    # Če ne moremo pridobiti piškotka, ker je uporabnik nov: 
    except:
        id_piskotek = streznik.nova_igra(standardne_ladje)
        bottle.response.set_cookie(
            'id_igre', str(id_piskotek), secret=SKRIVNOST, path='/')
    if id_piskotek is None:
        id_piskotek = streznik.nova_igra(standardne_ladje)
        bottle.response.set_cookie(
            'id_igre', str(id_piskotek), secret=SKRIVNOST, path='/')
    return id_piskotek

def pridobi_igro():
    id_igre = streznik.igre.get(id())
    if id_igre is None:
        index = streznik.nova_igra(standardne_ladje)
        
        bottle.response.set_cookie('id_igre', str(
            index), secret=SKRIVNOST, path='/')
        print(streznik.igre[index])
        return streznik.igre[index]

    return id_igre

# V mapi static so css datoteke. 
@bottle.route('/static/<filename>', name='static')
def server_static(filename):
    return bottle.static_file(filename, root='static')

@bottle.get('/') # Ta del ne potrebuje piškotkov. 
def domov_get():
    return bottle.template('domov.html', get_url=bottle.url)

@bottle.get('/domov/') # Ta del ne potrebuje piškotkov. 
def domov_get():
    bottle.redirect('/')

@bottle.get('/postavljanje_offline/')
def igra_get():
    igra = pridobi_igro()[0]
    print(igra)
    return bottle.template('postavljanje.html', get_url=bottle.url, igra=igra, na_vrsti=igra.igralec_na_vrsti)

@bottle.get('/navodila/')
def navodila_get():
    return bottle.template('navodila.html', get_url=bottle.url)

@bottle.post('/postavi_offline/')
def offline_post():
   
    igra = pridobi_igro()[0] 
    ime_gumba = list(bottle.request.forms.keys())[0]  # 'i_j' , '1_4'


    if igra.indeks_trenutne_ladjice == -1:
        if ime_gumba == "spremeni_postavitev":
            igra.trenutna_postavitev = not igra.trenutna_postavitev
            bottle.redirect('/postavljanje_offline/')
        
        if ime_gumba == 'naslednji_igralec':
            igra.indeks_trenutne_ladjice = 0
            igra.igralec_na_vrsti = igra.igralec_na_vrsti + 1
            if  igra.igralec_na_vrsti >= 2:
                igra.igralec_na_vrsti = 0
                igra.indeks_trenutne_ladjice = 0
                bottle.redirect('/igra_offline/')
            else:
                bottle.redirect('/postavljanje_offline/')
        
        else:
            bottle.redirect('/postavljanje_offline/') 
    
    if ime_gumba == 'naslednji_igralec':
            igra.indeks_trenutne_ladjice = 0
            igra.igralec_na_vrsti = igra.igralec_na_vrsti + 1
            if  igra.igralec_na_vrsti >= 2:
                igra.igralec_na_vrsti = 0
                igra.indeks_trenutne_ladjice = 0
                bottle.redirect('/igra_offline/')
            else:
                bottle.redirect('/postavljanje_offline/')
    if ime_gumba == "spremeni_postavitev":
        igra.trenutna_postavitev = not igra.trenutna_postavitev
        bottle.redirect('/postavljanje_offline/')
    else:
        vrstica = int(ime_gumba.split('_')[0])
        stolpec = int(ime_gumba.split('_')[1])
        postavitev = igra.trenutna_postavitev
        uspesnost = igra.postavi(postavitev, vrstica, stolpec, igra.indeks_trenutne_ladjice, igra.igralec_na_vrsti)

        if not uspesnost:
            bottle.redirect('/postavljanje_offline/')

        # Povečamo indeks, da postavimo naslednjo ladjico. 
        igra.indeks_trenutne_ladjice = igra.indeks_trenutne_ladjice + 1
        print(igra.indeks_trenutne_ladjice)

        # Preverimo ali je igralec postavil že vse svoje ladjice. 
        if igra.indeks_trenutne_ladjice >= len(igra.ladjice[0]):
            igra.indeks_trenutne_ladjice = -1
            # igra.igralec_na_vrsti = igra.igralec_na_vrsti + 1

        # Preverimo ali sta že oba igralca posatvila ladjice.
        if igra.igralec_na_vrsti in range(0, 2):
            bottle.redirect('/postavljanje_offline/')
        else:
            bottle.redirect('/navodila/') #potem premaknem na kaj drugega, zaenkrat tko samo tok da vidm, drugo polje!!!
        

    #igra.index += 1 oziroma ga daš na 0, če je velčji od dolžine tabele
    #če g daš na 0, greš nanaslednjega igralca
    #če si na zadnjem igralcu, se premakneš na /igra_offline/ al pa kej potobnega
@bottle.get('/igra_offline/')
def igra_get():
    igra = pridobi_igro()[0]
    return bottle.template('igra.html', get_url=bottle.url, igra=igra, na_vrsti=igra.igralec_na_vrsti, tekst='' )
@bottle.get('/igra_offline/<tekst>')
def igra_get(tekst):
    igra = pridobi_igro()[0]
    return bottle.template('igra.html', get_url=bottle.url, igra=igra, na_vrsti=igra.igralec_na_vrsti, tekst=str(tekst) )
@bottle.post('/igraj_offline/')
def igraj_offline():
    igra = pridobi_igro()[0]
    ime_gumba = list(bottle.request.forms.keys())[0]
    if igra.indeks_trenutne_ladjice == -1: # smo že naredili potezo in zdj čakamo, da tipo pritisne gumb naslednji igralec
        if ime_gumba == 'naslednji_igralec':
            igra.indeks_trenutne_ladjice = 0
            igra.igralec_na_vrsti = not igra.igralec_na_vrsti
        bottle.redirect('/igra_offline/')
    if igra.indeks_trenutne_ladjice == -2:
        if ime_gumba == 'naslednji_igralec':
            igra.indeks_trenutne_ladjice = 0
            igra.igralec_na_vrsti = not igra.igralec_na_vrsti
        bottle.redirect('/domov/')
    vrstica = int(ime_gumba.split('_')[0])
    stolpec = int(ime_gumba.split('_')[1])
    # nuklearka mejbi opcija ?
    poteza = igra.poteza(not igra.igralec_na_vrsti, vrstica, stolpec)
    if poteza == 'zmaga':
        print('reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        igra.indeks_trenutne_ladjice = -2
    else:
        igra.indeks_trenutne_ladjice = -1
    bottle.redirect(f'/igra_offline/{poteza}')

    

    bottle.redirect('/igra_offline/')
@bottle.get('/nastavitve/<n>')
def nastaviktve(n):
        igra = pridobi_igro()[0]
        return bottle.template('nastavitve.html', get_url=bottle.url, korak=n, igra=igra)

@bottle.post('/nastavi_velikost/')
def f():
    stevilo = int(bottle.request.forms['quantity'] )
    igra = pridobi_igro()[0]
    igra.standardne_ladje = [2] * stevilo
    bottle.redirect('/nastavitve/for')

@bottle.post('/nastavi_dolzino/')
def f():
    stevilo = int(bottle.request.forms['quantity']) 
    igra = pridobi_igro()[0]
    igra.standardne_ladje[igra.indeks_trenutne_ladjice] = stevilo
    igra.indeks_trenutne_ladjice += 1
    if igra.indeks_trenutne_ladjice >= len(igra.standardne_ladje):
        igra.indeks_trenutne_ladjice = 0
        bottle.redirect('/domov/')
    bottle.redirect('/nastavitve/for')

@bottle.post('/nova_igra/')
def zgodovina_post():
    ime_gumba = list(bottle.request.forms.keys())[0]
    if ime_gumba == 'offline':  # Pritisnil je prvi gumb. 
        igra = pridobi_igro()[0]
        # print(f'igra: {type(igra)}')
        igra.__init__(igra.standardne_ladje) # Začnemo NOVO igro. 
        bottle.redirect('/postavljanje_offline/')
    if ime_gumba == 'nastavitve':
        igra = pridobi_igro()[0]
        bottle.redirect('/nastavitve/velikost')
    else:
        pass
        #online
    
bottle.run(debug=True, reloader=True, host='localhost')

'''
TODO : 

potem ko en igralec postavi svoje ladjice, pokaži novo polje še za drugega

self.trenutni index ladice in self. na vrsti je  daš v Igra(), in potem model.Igra() vednio ve , kdo je na vrsti in katero ladijco postavljamo

nato funkcija postavi offline



na koncu naj se izpiše zmagovalec

lep html

'''