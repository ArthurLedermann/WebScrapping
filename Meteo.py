from webPageClass import WebPage
import WifiCheck as WC

cities = {"Toulouse":"Toulouse-Europe-France-Haute+Garonne-LFBO-1-26128.html",
          "CESI":"Toulouse-Europe-France-Haute+Garonne-LFBO-1-26128.html",
          "Papa":"Pau-Europe-France-Pyrenees+Atlantiques-LFBP-1-26113.html",
          "Maman":"Pau-Europe-France-Pyrenees+Atlantiques-LFBP-1-26113.html"}

class Meteo(WebPage):

    def __init__(self):

        Connection = WC.ConnectedWifi()
        Connection.recognizeWifi()

        self.url = 'https://www.tameteo.com/meteo_' + cities[Connection.location]

    def meteoToday(self):
        self.heures = self.soup.find_all("span", class_="hora")        
        self.temperatures = self.soup.find_all("td", class_="temperatura changeUnitT")

        self.heures = self.sortSoup(self.heures)
        self.temperatures = self.sortSoup(self.temperatures)

        self.meteoTodayTemp = []

        for i in range(len(self.temperatures)):
            self.meteoTodayTemp.append((self.heures[i], self.temperatures[i]))

    def maxMin(self, day):
        self.extremum = ['<span class="maxima changeUnitT"',
                         '<span class="minima changeUnitT"']

        self.tomorrow = str(self.soup.find_all("li", class_="dia " + day))

        self.meteoMaxMin = []

        for ext in self.extremum:
            self.tempo = self.tomorrow[self.tomorrow.index(ext):]
            self.meteoMaxMin.append(self.sortSoup(self.tempo))

        return self.meteoMaxMin



if __name__ == "__main__":

    test = Meteo()
    test.updatePage()
    test.meteoToday()
    maxTomorrow = test.maxMin("d1 activo")

    print(test.meteoTodayTemp)
    print(maxTomorrow)
