from selenium import webdriver
from bs4 import BeautifulSoup
import os


class WebPage():

    def updatePage(self):
        self.driver = webdriver.Chrome(str(os.path.dirname(os.path.abspath(__file__))) + "\Ressources\Programmes\chromedriver.exe")
        
        self.driver.get(self.url)
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')

        self.driver.close()

    def sortSoup(self, soupString, start=">", startAdd=0, end="<", endAdd = 0, replace=True):

        keep = soupString

        try:
            soupString=list(soupString)

            self.soupString = []

            for i in range(len(soupString)):

                self.soupString.append(str(soupString[i]))

                j = self.soupString[i].index(start) + 1 +startAdd
                k = j + self.soupString[i][j:].index(end) + endAdd
                self.soupString[i] = self.soupString[i][j:k]

                if replace:
                    self.soupString[i] = self.soupString[i].replace("\n", "").replace(" ", "")

            return self.soupString

        except:

            soupString = keep

            if type("Test")==type(soupString):

                self.soupString = soupString

                j = self.soupString.index(start) + 1 + startAdd
                k = j + self.soupString[j:].index(end) + endAdd
                self.soupString = self.soupString[j:k]

                if replace:
                    self.soupString = self.soupString.replace("\n", "").replace(" ", "")

                return self.soupString

            else:

                self.soupString = "Error sorting soup"

                return self.soupString
