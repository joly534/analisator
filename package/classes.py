import requests
import tkinter as tk
from bs4 import BeautifulSoup

class PageWeb:
    def __init__(self, url):
        self.r = requests.get(url)  
        self.html = self.r.text
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.pretty = self.soup.prettify()
        self.title = self.soup.title.string
        self.code = self.r.status_code

    def getLinks(self):
        for link in self.html.find_all('a'):
            links = link.get('href')
            return links
            
    def getMenu(self):
        for menu in self.soup.find_all('li'):
            menus = menu.text
            print(menus)

    def getSEO(self):
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
        canvas.create_rectangle(self.x,self.y,self.dx,self.dy,fill=self.color)       

    def textInside(self, canvas, title):
        canvas.create_text ((self.tx, self.ty), text=title, anchor='w')


