from tkinter import Label, LabelFrame, Scrollbar, Listbox
from typing import Text
from package.functions import *
import requests
from bs4 import BeautifulSoup

class Onglet:
    def __init__(self, root, title, data):
        #creation d'un onglet
        self.resultScreen = Listbox(root, width='1200', fg='black')
        self.resultScreen.pack()

        #ajout de la barre de scroll
        self.scroll = Scrollbar(self.resultScreen, command=self.resultScreen.yview)
        self.scroll.pack()

        #configuration de la typo
        self.resultScreen.configure(font='System')
        self.resultScreen.configure(yscrollcommand=self.scroll.set)

        #ajout de l'onglet a la fenetre
        root.add(self.resultScreen, text=title)


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