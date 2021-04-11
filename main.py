from package.functions import *

siteWeb = []


# ANALISONS LE SITE WEB
def analise():
    head = "https://"
    saisie_url = entry.get()
    for char in saisie_url:
        if saisie_url[0] != "h" and saisie_url[1] != "t" and saisie_url[2] != "t" and saisie_url[3] != "p" and saisie_url[4] != ":" and saisie_url[5] != "/" and saisie_url[6] != "/":
            saisie_url = head + saisie_url
    pageweb = PageWeb(saisie_url)
    if pageweb.code != 200:
        erreur = tk.Label(root, text="La page web à l'adresse : " + saisie_url + " a renvoyé une erreur " + pageweb.code + " . \n Verifiez l'orthographe de l'Url que vous avez saisi ou contactez l'administrateur de ce site pour obtenir plus d'infos.")
        erreur.pack()
    else:
        showresult(pageweb.soup, saisie_url, root)


#############################################################################
################## FENETRE PRINCIPALE DU PROGRAMME ##########################
#############################################################################
root = tk.Tk()                                                              #
root.title("Analiseur de site web")                                         #
root.geometry('1200x600')                                                   #
### FENETRE CONTENANT LA DEMANDE DE SAISIE DE L'URL DU SITE                 #
url_window = tk.Frame(root)                                                 #
url_window.pack()                                                           #
labelUrl = tk.Label(url_window, text="Entrez l'URL du site à analiser")     #
labelUrl.pack(side='left')                                                  #
### DEMANDE DE SAISIE DE L'URL A ANALISER                                   #
entry = tk.Entry(url_window, width=60)                                    #
######################### URL DE TEST #######################################
adresse = 'https://ekeipsi-medias.fr'                                       #
entry.insert(tk.END, adresse)                                                #
#############################################################################
entry.pack(side='left')                                                     #
### BOUTON POUR LANCER L'ANALISE                                            #
bouton_url = tk.Button(url_window, text="Analyser", command=analise)        #
bouton_url.pack(side='left')                                                #
### MENU DE LA FENTERE DES RESULTATS                                       #
menu = tk.Frame(root, bg='grey')                                       #
menu.pack()                                       #
### BOUTON HTML                                       #
bouton_html = tk.Button(menu, text="HTML", command=showhtml)
bouton_html.pack(side='left')
### BOUTON SEO
bouton_seo = tk.Button(menu, text="SEO", command=showseo)
bouton_seo.pack(side='left')
### BOUTON LIENS
bouton_liens = tk.Button(menu, text="LIENS", command=showlinks)                                      #
bouton_liens.pack(side='left')                                       #
### BOUTON ORGANIGRAMME                                       #
bouton_organigramme = tk.Button(menu, text="ORGANIGRAMME", command=showorganigram)  #
bouton_organigramme.pack(side='left')                                       #
root.mainloop()                                        #
###################################################################################
###################################################################################
