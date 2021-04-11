import tkinter as tk
import time
import threading
from tkinter import ttk
from package.classes import PageWeb

#AFFICHONS LE CODE HTML
def showhtml(root, data):
    ### CREATION DE LA FENTETRE
    htmlScreen = tk.Text(root, width='1200')
    htmlScreen.pack()
    root.update_idletasks()
    time.sleep(0.1)
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
        root.update_idletasks()
        time.sleep(0.1)
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

def showprogressbar(root):
    analiseprogress = ttk.Progressbar(root, length=100, mode='indeterminate')
    analiseprogress.pack(side='top')
    root.update_idletasks()


# AFFICHONS LE RESULTAT DANS LA FENETRE
def showresult(content, url, root):
    showprogressbar(root)
    ### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE

    resultWindow = ttk.Notebook(root, width="1200")
    resultWindow.pack()

    # ON AJOUTE L'ASYNCHRONE
    th_html = threading.Thread(target=showhtml(resultWindow, content))
    th_links = threading.Thread(target=showlinks(resultWindow, content))

    th_html.start()
    th_links.start()

    th_html.join()
    th_links.join()

    
    labelScreenWindow = tk.Label(root, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

