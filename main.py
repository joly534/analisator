import tkinter as tk
import sys
from package.classes import PageWeb, Rectangle
from package.functions import *

siteWeb=[]

# ANALISONS LE SITE WEB
def analise():
    saisie_url = entry.get()
    pageWeb = PageWeb(saisie_url)
    # showResult(pageWeb.pretty, saisie_url, root)
    showResult(pageWeb.getLinks, saisie_url, root)

    # pageWeb.getMenu()
    # siteWeb.append(pageWeb.r)
    # drawContent(pageWeb.title)


### FENETRE PRINCIPALE DU PROGRAMME #########################################
root = tk.Tk()                                                              #
root.title("Analiseur de site web")                                         #
root.geometry('1200x600')
### FENETRE CONTENANT LA DEMANDE DE SAISIE DE L'URL DU SITE                 #
url_window = tk.Frame(root)                                                 #
url_window.pack()                                                           #
labelUrl= tk.Label (url_window, text="""Entrez l'URL du site à analiser""") #
labelUrl.pack(side='left')                                                             #
### DEMANDE DE SAISIE DE L'URL A ANALISER                                   #
entry = tk.Entry (url_window, width= 60)                                    #
######################### URL DE TEST                                       #
adresse = 'https://ekleipsi-medias.fr'                                      #
entry.insert(tk.END,adresse)                                                #
####################################                                        #
entry.pack(side='left')                                                                #
### BOUTON POUR LANCER L'ANALISE                                            #
bouton_url = tk.Button(url_window, text="Analyser", command=analise)        #
bouton_url.pack(side='left')                                                           #
root.mainloop()                                                             #
#############################################################################





