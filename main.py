#coding 
from tkinter import Scrollbar
from package.functions import *
from package.classes import *

# ANALISONS L'URL
def analise():
    head = "https://"
    saisie_url = entry.get()

    for char in saisie_url:
        if saisie_url[0] != "h" and saisie_url[1] != "t" and saisie_url[2] != "t" and saisie_url[3] != "p" \
           and saisie_url[4] != ":" and saisie_url[5] != "/" and saisie_url[6] != "/":
            saisie_url = head + saisie_url
            
    pageweb = PageWeb(saisie_url)
    title = pageweb.title
    
    # FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
    resultWindow = ttk.Notebook(root, width="1200")
    resultWindow.pack()

    if pageweb.code != 200:
        erreur = tk.Label(root, text="La page web à l'adresse : " + saisie_url + " a renvoyé une erreur " + pageweb.code +
                " . \n Verifiez l'orthographe de l'Url que vous avez saisi ou contactez l'administrateur de ce site pour obtenir plus d'infos.")
        erreur.pack()
    else:
        onglet = Onglet(resultWindow, title, pageweb.soup)
        showlinks(onglet.labelLinksFrame, pageweb.soup)
    
        #showresult(pageweb.pretty, saisie_url, root, title, pageweb.soup)


#####################################################################################
################## FENETRE PRINCIPALE DU PROGRAMME ##################################
#####################################################################################
root = tk.Tk()                                                                      #
root.title("Analisator 3000")                                                       #
root.geometry('1200x600+0+0')                                                       #
### FENETRE CONTENANT LA DEMANDE DE SAISIE DE L'URL DU SITE                         #
url_window = tk.Frame(root)                                                         #
url_window.pack()                                                                   #
labelUrl = tk.Label(url_window, text="Entrez l'URL du site à analiser")             #
labelUrl.pack(side='left')                                                          #
### DEMANDE DE SAISIE DE L'URL A ANALISER                                           #
entry = tk.Entry(url_window, width=60)                                              #
######################### URL DE TEST ###############################################
adresse = 'https://ekleipsi-medias.fr'                                              #
entry.insert(tk.END, adresse)                                                       #
#####################################################################################
entry.pack(side='left')                                                             #
### BOUTON POUR LANCER L'ANALISE                                                    #
bouton_url = tk.Button(url_window, text="Analyser", command=analise)                #
bouton_url.pack(side='left')                                                        #
root.mainloop()                                                                     #
#####################################################################################
#####################################################################################