from os import replace
from webPageClass import WebPage
import datetime, requests, os

numbers = {0:"First",
           1:"Second",
           2:"Third"}


class SpaceFlightsInformations(WebPage):

    def __init__(self):
        self.url = 'https://nextspaceflight.com/'

    def getNextFlightsBuisness(self):
        nextFlightsBuisnessPageHard = list(self.soup.find_all('span'))

        nextFlightsBuisnessPage = []
        for i in [1, 3, 5]:
            nextFlightsBuisnessPage.append(nextFlightsBuisnessPageHard[i])

        self.nextFlightsBuisness = self.sortSoup(nextFlightsBuisnessPage)
        for i in range(len(self.nextFlightsBuisness)):
            self.nextFlightsBuisness[i] = self.nextFlightsBuisness[i].replace("\t", "")

    def getNextFlightsRocketsNames(self):
        nextFlightsRocketsNamePage = self.soup.find_all('h5', attrs={'class', 'header-style'})

        self.nextFlightsRocketsName = self.sortSoup(nextFlightsRocketsNamePage, end="|")

    def getNextFlightsDates(self):
        self.nextFlightsDates = list(self.soup.find_all('div', attrs={'class', 'mdl-card__supporting-text'}))[:3]

        date = datetime.date.today()
        year = date.strftime("%Y")

        for i in range(len(self.nextFlightsDates)):
            if "NET" in str(self.nextFlightsDates[i]):
                self.nextFlightsDates[i]=self.sortSoup(str(self.nextFlightsDates[i]), start="NET", startAdd=-1, end=year, endAdd=4, replace=False)
            elif "UTC" in str(self.nextFlightsDates[i]):
                self.nextFlightsDates[i]=self.sortSoup(str(self.nextFlightsDates[i]), start="\n", startAdd=53, end="UTC", endAdd=3, replace=False)
            else:
                self.nextFlightsDates[i] = "Error extracting data"

    def getImageURl(self):
        self.imageUrl = self.soup.find_all('div', attrs={'class', 'mdl-cell mdl-cell--6-col'})
        self.imageUrl = self.sortSoup(self.imageUrl, start="url(", startAdd=3, end=")")

    def getImage(self):
        self.getImageURl()
        for i in range(len(self.imageUrl)):
            r = requests.get(self.imageUrl[i])
            with open(str(os.path.dirname(os.path.abspath(__file__))) + "\Ressources\Images\ " + numbers[i]+ "Flight.jpg", "wb") as f:
                f.write(r.content)

    def getNextFlights(self):
        self.updatePage()

        self.getNextFlightsBuisness()
        self.getNextFlightsRocketsNames()
        self.getNextFlightsDates()
        self.getImage()


 

if __name__ == "__main__":
    
    test = SpaceFlightsInformations()
    test.getNextFlights()
    
    print(test.nextFlightsBuisness)
    print(test.nextFlightsRocketsName)
    print(test.nextFlightsDates)