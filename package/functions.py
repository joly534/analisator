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
    bouton_html.pack(side='left')

    ### BOUTON SEO
    bouton_seo = tk.Button(menu, text="SEO", command=showSeo)
    bouton_seo.pack(side='left')

    ### BOUTON LIENS
    bouton_liens = tk.Button(menu, text="LIENS", command=showLinks)
    bouton_liens.pack(side='left')

    ### BOUTON ORGANIGRAMME
    bouton_organigramme = tk.Button(menu, text="ORGANIGRAMME", command=showOrganigram)
    bouton_organigramme.pack(side='left')



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
    resultWindow = tk.Frame(root, width="1200")
    resultWindow.pack()
    showLinks(resultWindow,content)
    # showMenu(resultWindow, content) 
    # showHtml(resultWindow, content) 
    labelScreenWindow = tk.Label(root, text='Resultat de la requete pour ' + url)
    labelScreenWindow.pack()         

