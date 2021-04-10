import requests
from bs4 import BeautifulSoup


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
            print(menus)

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
