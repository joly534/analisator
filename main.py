import urllib3  
import tkinter as tk
import tkinter.scrolledtext as st
import os
import sys
from functions.functions import statusUrl

from urllib3 import request



### FENETRE PRINCIPALE DU PROGRAMME
root = tk.Tk()
root.geometry("720x600")
root.title("Analiseur de site web")
### FENETRE CONTENANT L'ENTREE DE L'URL DU SITE A ANALISER ET LE RESULTAT DE LA REQUETTE
url_window =tk.Frame(root)                 
url_window.pack()
status= tk.Label (url_window, text="""Entrez l'URL du site à analiser""")           ### on crée une fenetre dans laquelle on affiche le status de la requette 
status.pack()
saisie_url=tk.Entry (url_window, width= 60)           ### on demande la saisie de l'url du site à analiser
saisie_url.pack()
bouton_url = tk.Button(url_window, text="Envoyer", command=statusUrl)      ### bouton pour lancer la requette
bouton_url.pack()
### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
screenWindow = tk.Frame(root)
screenWindow.pack()
textScreenWindow= st.ScrolledText(screenWindow)
textScreenWindow.pack()




root.mainloop()

