import tkinter as tk
import tkinter.scrolledtext as st
from package.classes import PageWeb

#AFFICHONS LE CODE HTML
def showHtml(root, data):
    ### CREATION DE LA FENTETRE
    htmlScreen = tk.Text(root, width='1200', bg='grey')
    htmlScreen.delete(1.0, 'end')
    htmlScreen.insert(1.0, data)
    htmlScreen.pack()

#AFFICHONS LE SEO
def showSeo(root):
    pass

#AFFICHONS LA LISTE DES LIENS
def showLinks(root, data):
    numberOfLinks = 0
    linkScreen = tk.Text(root, width="1200")
    linkScreen.pack()
    linkScreen.delete(1.0, 'end')
    for link in data.find_all('a'):
        pageweb = PageWeb(link.get('href'))
        linkScreen.insert(1.0, (link.get('href')) + ' ' + str(pageweb.code) + '\n')
        numberOfLinks += 1    
    linkScreen.insert(1.0, 'Il y a ' + str(numberOfLinks) + ' liens sur cette page. \n \n')

#AFFICHONS L'ORGANIGRAMME
def showOrganigram(root, title):
    ### FENETRE CONTENANT LE CANVAS
    canvas = tk.Canvas(root, width="1200")
    canvas.pack()
    # COMMENCONS A DESSINER UN ORGANIGRAME
    def drawContent(title):
        for i in siteWeb:
            rectangle = Rectangle(100,100,500,150,"yellow")
            rectangle.draw(canvas)
            rectangle.textInside(canvas, title)

# AFFICHONS LE RESULTAT DANS LA FENETRE
def showResult(content, url, root):
    ### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
    resultWindow = tk.Frame(root, width="1200")
    resultWindow.pack()
    showHtml(resultWindow, content) 
    # showLinks(resultWindow,content)

    
    labelScreenWindow = tk.Label(root, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

