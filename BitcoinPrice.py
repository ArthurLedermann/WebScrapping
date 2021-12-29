from webPageClass import WebPage

share=0.00142771

class BitCoin(WebPage):

    def __init__(self):
        self.url = 'https://www.bitcoinprice.com/'

    def getPrice(self):
        self.value = str(self.soup.find_all('span', id="price"))
        self.value = self.sortSoup(self.value)

    def getPercent(self):
        self.percent = str(self.soup.find_all('span', id="percent-change"))
        self.percent = self.sortSoup(self.percent)

class Wallet():
    
    def __init__(self, share=0.00142771, currencie=BitCoin()):
        self.share = float(share)
        self.currencie = currencie

    def updateCurrencie(self):
        self.currencie.updatePage()
        self.currencie.getPrice()
        self.currencie.getPercent()
        self.currencie.value = float(self.currencie.value.replace(",", "").replace("$", ""))

    def calculateValue(self):
        self.shareValue = self.share * self.currencie.value


if __name__ == "__main__":

    test = Wallet(share, BitCoin())
    test.updateCurrencie()
    test.calculateValue()
    print(test.currencie.value)
    print(test.currencie.percent)
    print(test.shareValue)




