import tkinter as tk
import time
import threading
from tkinter import ttk
from package.classes import PageWeb, Rectangle


# AFFICHONS LE CODE HTML
def showhtml(root, data):
    # CREATION DE LA FENETRE
    htmlscreen = tk.Text(root, width='1200')
    htmlscreen.pack()
    root.update_idletasks()
    time.sleep(0.1)
    root.add(htmlscreen, text="HTML")
    htmlscreen.delete(1.0, 'end')
    htmlscreen.insert(1.0, data)


# AFFICHONS LE SEO
def showseo(root):
    pass


# AFFICHONS LA LISTE DES LIENS
def showlinks(root, data):
    numberoflinks = 0
    linkscreen = tk.Text(root, width="1200")
    linkscreen.pack()
    root.add(linkscreen, text="Liens de la page")
    linkscreen.delete(1.0, 'end')
    # LISTONS TOUS LES LIENS
    for link in data.find_all('a'):
        pageweb = PageWeb(link.get('href'))
        linkscreen.insert(1.0, (link.get('href')) + ' ' + str(pageweb.code) + '\n')
        root.update_idletasks()
        time.sleep(0.1)
        numberoflinks += 1
    linkscreen.insert(1.0, 'Il y a ' + str(numberoflinks) + ' liens sur cette page. \n \n')


# AFFICHONS L'ORGANIGRAMME
def showorganigram(root, data, title):
    # FENETRE CONTENANT LE CANVAS
    canvas = tk.Canvas(root, width="1200", height="1000", bg='black')
    canvas.pack()

    # DESSINONS LES MODELES DE REFERENCE
    pendingrectangle = Rectangle(1000,10,1150,50, "#ffd700")
    pendingrectangle.draw(canvas)
    validaterectangle = Rectangle(1000, 60, 1150, 100, "#00ff00")
    validaterectangle.draw(canvas)
    refusedrectangle = Rectangle(1000, 110, 1150, 150, "#fe1b00")
    refusedrectangle.draw(canvas)
    validaterectangle.textinside(canvas, "Status OK" )
    pendingrectangle.textinside(canvas, "En cours...")
    refusedrectangle.textinside(canvas, "Erreur de lien")
    root.update_idletasks()
    time.sleep(0.1)

    # COMMENCONS A DESSINER L'ORGANIGRAME
    x = 50
    y = 50
    dx = 420
    dy = 90
    rectangle = Rectangle(x, y, dx, dy, "#00ff00")
    rectangle.draw(canvas)
    rectangle.textinside(canvas, title)
    for link in data.find_all('a'):
        titlelink = link.text
        y += 50
        dy += 50
        rectangle = Rectangle(x, y, dx, dy, "#ffd700")
        rectangle.draw(canvas)
        rectangle.textinside(canvas, titlelink)
        root.update_idletasks()
        time.sleep(0.1)

def showprogressbar(root):
    analiseprogress = ttk.Progressbar(root, length=100, mode='indeterminate')
    analiseprogress.pack(side='top')
    root.update_idletasks()


# AFFICHONS LE RESULTAT DANS LA FENETRE
def showresult(content, url, root, title):
    showprogressbar(root)

    # FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
    resultWindow = ttk.Notebook(root, width="1200")
    resultWindow.pack()

    # ON AJOUTE L'ASYNCHRONE
    # th_html = threading.Thread(target=showhtml(resultWindow, content))
    # th_links = threading.Thread(target=showlinks(resultWindow, content))
    th_organigram = threading.Thread(target=showorganigram(resultWindow, content, title))

    # th_html.start()
    # th_links.start()
    th_organigram.start()

    # th_html.join()
    # th_links.join()
    th_organigram.join()

    
    labelScreenWindow = tk.Label(root, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

