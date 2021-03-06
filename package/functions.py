import tkinter as tk
import time
import threading
from tkinter import Label, ttk, scrolledtext, font
from package.classes import PageWeb, Rectangle


# AFFICHONS LE CODE HTML
def showhtml(root, data):
    # CREATION DE LA FENETRE
    htmlscreen = scrolledtext.ScrolledText(root, width='1200', bg='black', fg='white')
    htmlscreen.pack()
    htmlscreen.configure(font='System')
    time.sleep(0.1)
    # LIBELE DE LA FRAME
    root.add(htmlscreen, text="HTML")
    htmlscreen.delete(1.0, 'end')
    htmlscreen.insert(1.0, data)
    root.update_idletasks()
    progresshtml = ttk.Progressbar(htmlscreen, length=100, mode='indeterminate')
    progresshtml.pack()


# AFFICHONS LE SEO
def showseo(root):
    pass


# AFFICHONS LA LISTE DES LIENS
def showlinks(root, data):
    # LISTONS TOUS LES LIENS    
    for link in data.find_all('a'):
        pageweb = PageWeb(link.get('href'))
        contentLinks = (link.get('href')) + ' ' + str(pageweb.code) + '\n'
        lbl = Label(root, text=contentLinks)
        lbl.pack()
        #root.insert(1.0, (link.get('href')) + ' ' + str(pageweb.code) + '\n')
        lbl.update_idletasks()
        time.sleep(0.1)


# AFFICHONS L'ORGANIGRAMME
def showorganigram(root, data, title):
    # FENETRE CONTENANT LE CANVAS
    canvas = tk.Canvas(root, width="1200", height="1000", bg='black')
    canvas.pack()


    # LIBELE DE LA FRAME
    root.add(canvas, text="Organigramme")

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


# AFFICHONS LE RESULTAT DANS LA FENETRE
def showresult(content, url, root, title, soupe):

    # FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
    resultWindow = ttk.Notebook(root, width="1200")
    resultWindow.pack()

    # ON AJOUTE L'ASYNCHRONE
    th_html = threading.Thread(target=showhtml(resultWindow, content))
    #th_links = threading.Thread(target=showlinks(resultWindow, soupe))
    th_organigram = threading.Thread(target=showorganigram(resultWindow, soupe, title))

    th_html.start()
    #th_links.start()
    th_organigram.start()

    th_html.join()
    #th_links.join()
    th_organigram.join()

    
    labelScreenWindow = tk.Label(root, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

