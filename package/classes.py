import urllib3
import tkinter as tk
from urllib3 import request
from bs4 import BeautifulSoup

class PageWeb:
    def __init__(self, url):
        self.url = url  
        http = urllib3.PoolManager()
        self.reponse = http.request('GET',self.url)
        self.donnees = self.reponse.data
        self.pageDecode = self.donnees.decode('utf-8')
        self.page = BeautifulSoup(self.url, 'html.parser')
        self.balises = self.page.prettify()
        self.title = self.page.title
               
    def getStatus(self):
        status = self.reponse.status

    def drawContent(self):
        pass

    def followLink(self):
        pass

    def getSeo(self):
        pass



