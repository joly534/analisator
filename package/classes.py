import urllib3
import tkinter as tk
from urllib3 import request

class PageWeb:
    def __init__(self, url):
        self.url = url  
        self.balise = []
        http = urllib3.PoolManager()
        self.reponse = http.request('GET',self.url)
        self.donnees = self.reponse.data
        self.pageDecode = self.donnees.decode('utf-8')
               
    def getStatus(self):
        status = self.reponse.status

    def parseContent(self):
        i = 0
        j = 0
        for i, char in self.pageDecode:
            if self.pageDecode[i] != ">":
                self.balise[j].extend(self.pageDecode[i])
                i += 1
            if self.donnees[i] == ">":
                self.balise[j].extend(self.pageDecode[i])
                j += 1
                i += 1


    def drawContent(self):
        pass

    def followLink(self):
        pass

    def getSeo(self):
        pass



