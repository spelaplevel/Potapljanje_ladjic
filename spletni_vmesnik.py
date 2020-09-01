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

    ime_gumba = list(bottle.request.forms.keys())[0] # 'i_j' , '1_4'
    vrstica = int(ime_gumba.split('_')[0])
    stolpec = int(ime_gumba.split('_')[1])
    postavitev = int(ime_gumba.split('_')[2])
    igra.postavi(postavitev, vrstica, stolpec, 0, 0)

    #igra.index += 1 oziroma ga daš na 0, če je velčji od dolžine tabele
    #če g daš na 0, greš nanaslednjega igralca
    #če si na zadnjem igralcu, se premakneš na /igra_offline/ al pa kej potobnega

    bottle.redirect('/postavljanje_offline/')

@bottle.post('/nova_igra/')
def zgodovina_post():
    if list(bottle.request.forms.keys())[0] == 'offline':  # Pritisnil je prvi gumb. 
        igra = pridobi_igro()[0]
        print(f'igra: {type(igra)}')
        igra.__init__([3,2]) # Začnemo NOVO igro. 
        bottle.redirect('/postavljanje_offline/')
    else:
        pass
        #online
    
bottle.run(debug=True, reloader=True, host='localhost')

'''
TODO : 
v postavljanje morš dat neko opcijo da ibere a bo verikalna al horizontalna


self.trenutni index ladice in self. na vrsti je  daš v Igra(), in potem model.Igra() vednio ve , kdo je na vrsti in katero ladijco postavljamo

nato funkcija postavi offline

lep html

'''