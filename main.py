import urllib3  
import tkinter as tk
import tkinter.scrolledtext as st
import os
import sys

from urllib3 import request

class PageWeb:
    def __init__(self, url):
        self.url = url  
        http = urllib3.PoolManager()
        reponse = http.request('GET',self.url)
        donnees = reponse.data
        donnees.decode('utf-8')

    def readAndShowContent(self):
        textScreenWindow.delete('1.0', "end")
        textScreenWindow.insert(1.0,donnees)
        textScreenWindow.pack()
        labelScreenWindow = tk.Label(screenWindow, text='Resultat de la requete pour ' + saisieUrl)
        labelScreenWindow.pack()

def analise(saisie_url):
    print(saisie_url)
    pageWeb = PageWeb(saisie_url)
    pageWeb.readAndShowContent()



### FENETRE PRINCIPALE DU PROGRAMME
root = tk.Tk()
root.geometry("720x600")
root.title("Analiseur de site web")
### FENETRE CONTENANT L'ENTREE DE L'URL DU SITE A ANALISER ET LE RESULTAT DE LA REQUETTE
url_window =tk.Frame(root)                 
url_window.pack()
labelUrl= tk.Label (url_window, text="""Entrez l'URL du site à analiser""")           ### on crée une fenetre dans laquelle on affiche le status de la requette 
labelUrl.pack()
           ### on demande la saisie de l'url du site à analiser
saisie_url = tk.Entry (url_window, width= 60)
saisie_url.pack()
bouton_url = tk.Button(url_window, text="Analyser", command=analise(saisie_url))      ### bouton pour lancer la requette
bouton_url.pack()
### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
screenWindow = tk.Frame(root)
screenWindow.pack()
textScreenWindow= st.ScrolledText(screenWindow)




root.mainloop()

