from BitcoinPrice import Wallet
from Meteo import Meteo
from nextSpaceFlight import SpaceFlightsInformations

from InfoUI import Ui_MainWindow

from PyQt5 import QtWidgets
from datetime import date, datetime
import sys, os

week = {0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Satudray",
        6:"Sunday"}

class Interface:

    def __init__(self):
        self.bitcoin = Wallet()
        self.meteo = Meteo()
        self.rocketsFlights = SpaceFlightsInformations()

    def update(self):
        self.bitcoin.updateCurrencie()
        self.bitcoin.calculateValue()
        self.meteo.updatePage()
        self.meteo.meteoToday()
        self.meteo.maxMin("d1 activo")
        self.rocketsFlights.getNextFlights()
        os.system('cmd /c "pyrcc5 FlightsImages.qrc -o FlightsImages.py"')

    def createWindow(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        self.ui = Ui_MainWindow()

    def formatData(self):
        self.bitcoinPrice = str(round(self.bitcoin.currencie.value, 2))
        self.bitcoinPrice = self.bitcoinPrice[:self.bitcoinPrice.index(".")-3] + "," + self.bitcoinPrice[self.bitcoinPrice.index(".")-3:]
        self.bitcoin.shareValue = str(round(self.bitcoin.shareValue, 2))

        tempo = []
        missing = 18-len(self.meteo.meteoTodayTemp)
        for i in range(18):
                if i<missing:
                        tempo.append(('Passé', "Ø°"))
                else:
                        tempo.append((self.meteo.meteoTodayTemp[i-missing][0], self.meteo.meteoTodayTemp[i-missing][1]))

        self.meteo.meteoTodayTemp = tempo

        self.todayWeek = week[datetime.today().weekday()] + " " + str(datetime.today().day)
        self.time = str(datetime.today().hour) + ":" + str(datetime.today().minute)


    def showWindow(self):
        self.ui.setupUi(self.MainWindow, self.bitcoinPrice, self.bitcoin.currencie.percent, self.bitcoin.shareValue, self.rocketsFlights.nextFlightsRocketsName, self.rocketsFlights.nextFlightsBuisness, self.rocketsFlights.nextFlightsDates, self.meteo.meteoTodayTemp, self.meteo.meteoMaxMin, self.todayWeek, self.time)
        self.MainWindow.show()
        sys.exit(self.app.exec_())

 
if __name__ == "__main__":

    test=Interface()
    test.update()
    test.formatData()
    test.createWindow()
    test.showWindow()