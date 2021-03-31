

def statusUrl(saisie_url): 
    saisieUrl = saisie_url.get()
    http = urllib3.PoolManager()
    reponse = http.request('GET', saisieUrl)
    donnees = reponse.data
    donnees.decode('utf-8')
    textScreenWindow.delete('1.0', "end")
    textScreenWindow.insert(1.0,donnees)
    labelScreenWindow = tk.Label(screenWindow, text='Resultat de la requete pour ' + saisieUrl)
    labelScreenWindow.pack()

def Test():
    i = 0
    while i < 5:    
        print(saisieUrl)   
        i += 1