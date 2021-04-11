import tkinter as tk
import time
from tkinter import ttk
from package.classes import PageWeb

#AFFICHONS LE CODE HTML
def showhtml(root, data):
    ### CREATION DE LA FENTETRE
    htmlScreen = tk.Text(root, width='1200')
    htmlScreen.pack()
    root.add(htmlScreen, text="HTML")
    htmlScreen.delete(1.0, 'end')
    htmlScreen.insert(1.0, data)

#AFFICHONS LE SEO
def showseo(root):
    pass

#AFFICHONS LA LISTE DES LIENS
def showlinks(root, data):
    numberOfLinks = 0
    linkScreen = tk.Text(root, width="1200")
    linkScreen.pack()
    root.add(linkScreen, text="Liens de la page")
    linkScreen.delete(1.0, 'end')
    for link in data.find_all('a'):
        pageweb = PageWeb(link.get('href'))
        linkScreen.insert(1.0, (link.get('href')) + ' ' + str(pageweb.code) + '\n')
        numberOfLinks += 1    
    linkScreen.insert(1.0, 'Il y a ' + str(numberOfLinks) + ' liens sur cette page. \n \n')

#AFFICHONS L'ORGANIGRAMME
def showorganigram(root, title):
    ### FENETRE CONTENANT LE CANVAS
    canvas = tk.Canvas(root, width="1200")
    canvas.pack()
    # COMMENCONS A DESSINER UN ORGANIGRAME
    def drawcontent(title):
        for i in siteWeb:
            rectangle = Rectangle(100,100,500,150,"yellow")
            rectangle.draw(canvas)
            rectangle.textInside(canvas, title)

# AFFICHONS LE RESULTAT DANS LA FENETRE
def showresult(content, url, root):
    analiseprogress = ttk.Progressbar(root, length=100, mode='determinate')
    analiseprogress.pack()
    ### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
    resultWindow = ttk.Notebook(root, width="1200")
    resultWindow.pack()
    showhtml(resultWindow, content)
    #showlinks(resultWindow,content)

    
    labelScreenWindow = tk.Label(root, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

