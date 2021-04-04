import urllib3  
import tkinter as tk
import tkinter.scrolledtext as st
import os
import sys
from urllib3 import request
from package.classes import PageWeb

siteWeb=[]


def drawContent():
    i=0
    for i in siteWeb:
        canvas.create_rectangle(100,100,400,150, fill="yellow")


def showContent(content):
    textScreenWindow.delete('1.0', "end")
    textScreenWindow.insert(1.0,content)
    textScreenWindow.pack()

def analise():
    saisie_url = entry.get()
    pageWeb = PageWeb(saisie_url)
    siteWeb.append(pageWeb)
    drawContent()
    showContent(pageWeb.title)
    print(pageWeb.balises)
    labelScreenWindow = tk.Label(screenWindow, text='')
    labelScreenWindow = tk.Label(screenWindow, text='Resultat de la requete pour ' + pageWeb.url)
    labelScreenWindow.pack()


### FENETRE PRINCIPALE DU PROGRAMME
root = tk.Tk()
root.geometry("1400x900")
root.title("Analiseur de site web")

### FENETRE CONTENANT L'ENTREE DE L'URL DU SITE A ANALISER ET LE RESULTAT DE LA REQUETTE
url_window =tk.Frame(root)
url_window.pack()

### on crée une fenetre dans laquelle on affiche le status de la requette
labelUrl= tk.Label (url_window, text="""Entrez l'URL du site à analiser""")
labelUrl.pack()

### on demande la saisie de l'url du site à analiser
entry = tk.Entry (url_window, width= 60)

######################### url de test
adresse = 'ekleipsi-medias.fr'
entry.insert(tk.END,adresse)
####################################

entry.pack()

### bouton pour lancer la requette
bouton_url = tk.Button(url_window, text="Analyser", command=analise)
bouton_url.pack()

### FENETRE CONTENANT LE CANVAS
canvas = tk.Canvas(root, width="640", height="500", bg="grey")
canvas.pack(side='right')

### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
screenWindow = tk.Frame(root, width="640", height="500")
screenWindow.pack(side='left')
textScreenWindow= st.ScrolledText(screenWindow)








root.mainloop()

