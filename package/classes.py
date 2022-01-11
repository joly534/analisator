from tkinter import Label, LabelFrame
from typing import Text
from package.functions import *
import requests
from bs4 import BeautifulSoup

class Onglet:
    def __init__(self, root, title, data):
        #creation d'un onglet
        self.resultScreen = Label(root, width='1200', fg='black')
        self.resultScreen.pack()
        #configuration de la typo
        self.resultScreen.configure(font='System')
        #ajout de l'onglet a la fenetre
        root.add(self.resultScreen, text=title)

        #ajout de la partie sur le nombre de liens
        self.labelLinksFrame = LabelFrame(self.resultScreen, text='Liens présents sur cette page : ', height='300')
        self.labelLinksFrame.pack( fill="both", expand="yes")
        showLinks(self.labelLinksFrame, data)

        #ajout de la partie sur le SEO
        self.labelSEOFrame = LabelFrame(self.resultScreen, text='SEO de la page : ', height='300')
        self.labelSEOFrame.pack( fill="both", expand="yes")


class PageWeb:
    def __init__(self, url):
        self.r = requests.get(url)  
        self.html = self.r.text
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.pretty = self.soup.prettify()
        self.title = self.soup.title.string
        self.code = self.r.status_code

    def getmenu(self):
        for menu in self.soup.find_all('li'):
            menus = menu.text

    def getseo(self):
        pass           


class Rectangle:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.tx = self.x + 40
        self.ty = self.y + 20

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.dx, self.dy, fill=self.color)

    def textinside(self, canvas, title):
        canvas.create_text((self.tx, self.ty), text=title, anchor='w')