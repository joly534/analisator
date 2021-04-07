import tkinter as tk
import tkinter.scrolledtext as st
from package.classes import PageWeb



#AFFICHONS LE RESULTAT DE LA RECHERCHE
def showMenu(root):
    ### MENU DE LA FENTERE DES RESULTATS
    menu = tk.Frame(root, bg='grey')
    menu.pack()

    ### BOUTON HTML
    bouton_html = tk.Button(menu, text="HTML", command=showHtml)
    bouton_html.pack()

    ### BOUTON SEO
    bouton_seo = tk.Button(menu, text="SEO", command=showSeo)
    bouton_seo.pack()

    ### BOUTON LIENS
    bouton_liens = tk.Button(menu, text="LIENS", command=showLinks)
    bouton_liens.pack()

    ### BOUTON ORGANIGRAMME
    bouton_organigramme = tk.Button(menu, text="ORGANIGRAMME", command=showOrganigram)
    bouton_organigramme.pack()



#AFFICHONS LE CODE HTML
def showHtml(root, data):
    ### CREATION DE LA FENTETRE
    htmlScreen = st.ScrolledText(root, text=data, width='1280', bg='grey')
    htmlScreen.pack()

#AFFICHONS LE SEO
def showSeo(root):
    pass

#AFFICHONS LA LISTE DES LIENS
def showLinks():
    print('showLinks')

#AFFICHONS L'ORGANIGRAMME
def showOrganigram(root, title):
    ### FENETRE CONTENANT LE CANVAS
    canvas = tk.Canvas(root, width="1280")
    canvas.pack()
    # COMMENCONS A DESSINER UN ORGANIGRAME
    def drawContent(title):
        for i in siteWeb:
            rectangle = Rectangle(100,100,500,150,"yellow")
            rectangle.draw(canvas)
            rectangle.textInside(canvas, title)

# def showResult(content, root):
#     ### FENETRE CONTENANT LES RESULTATS DE LA REQUETTE
#     screen_result = tk.Frame(root, width="1280", height="500", bg='grey')
#     screen_result.pack()
#     textScreenWindow= st.ScrolledText(screenWindow, width="1280")
#     textScreenWindow.delete('1.0', "end")
#     textScreenWindow.insert(1.0, content)
#     textScreenWindow.pack()

# AFFICHONS LE RESULTAT DANS LA FENETRE
def showResult(content, url, root):
    ### FENETRE CONTENANT LE RESULTAT DE LA REQUETTE
    resultWindow = tk.Frame(root, width="1280")
    resultWindow.pack()
    showMenu(resultWindow) 
    showHtml(resultWindow, content) 
    labelScreenWindow = tk.Label(screenWindow, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

