import model
import bottle

streznik = model.Streznik()
SKRIVNOST = 'skrivnost'

standardne_ladje = [2,5]

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

@bottle.get('/postavljanje_offline/')
def igra_get():
    igra = pridobi_igro()
    print(igra)
    return bottle.template('postavljanje.html', get_url=bottle.url, igra=igra[0], na_vrsti=0)

@bottle.get('/navodila/')
def navodila_get():
    return bottle.template('navodila.html', get_url=bottle.url)

@bottle.post('/postavi_offline/')
def offline_post():
   
    igra = pridobi_igro()[0]
    indeks = igra.indeks_trenutne_ladjice
    igralec_na_vrsti = igra.igralec_na_vrsti
    ime_gumba = list(bottle.request.forms.keys())[0]  # 'i_j' , '1_4'

    if ime_gumba == "spremeni_postavitev":
        igra.trenutna_postavitev = not igra.trenutna_postavitev
        bottle.redirect('/postavljanje_offline/')
    else:
        vrstica = int(ime_gumba.split('_')[0])
        stolpec = int(ime_gumba.split('_')[1])
        postavitev = igra.trenutna_postavitev
        igra.postavi(postavitev, vrstica, stolpec, indeks, igralec_na_vrsti)

        # Povečamo indeks, da postavimo naslednjo ladjico. 
        igra.indeks_trenutne_ladjice = indeks + 1
        print(igra.indeks_trenutne_ladjice)

        # Preverimo ali je igralec postavil že vse svoje ladjice. 
        if igra.indeks_trenutne_ladjice in range(0, len(igra.ladjice[0])):
            pass
            print("Nismo še postavili vseh")
        else:
            igra.indeks_trenutne_ladjice = 0
            igra.igralec_na_vrsti = igralec_na_vrsti + 1

        # Preverimo ali sta že oba igralca posatvila ladjice.
        if igralec_na_vrsti in range(0, 2):
            bottle.redirect('/postavljanje_offline/')
        else:
            bottle.redirect('/navodila/') #potem premaknem na kaj drugega, zaenkrat tko samo tok da vidm, drugo polje!!!
        

    #igra.index += 1 oziroma ga daš na 0, če je velčji od dolžine tabele
    #če g daš na 0, greš nanaslednjega igralca
    #če si na zadnjem igralcu, se premakneš na /igra_offline/ al pa kej potobnega

@bottle.post('/nova_igra/')
def zgodovina_post():
    if list(bottle.request.forms.keys())[0] == 'offline':  # Pritisnil je prvi gumb. 
        igra = pridobi_igro()[0]
        print(f'igra: {type(igra)}')
        igra.__init__(standardne_ladje) # Začnemo NOVO igro. 
        bottle.redirect('/postavljanje_offline/')
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