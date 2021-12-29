import subprocess

pastConnections = {"SFR_1EC8":"Papa",
                   "HUAWEI-E5180-FAB2":"Maman",
                   "Wifirst JdS Toulouse Labege":"Toulouse",
                   "CESI_HotSpot":"CESI",
                   "LouLou":"CESI"}

pastConnectionsKeys = list(pastConnections.keys())

class ConnectedWifi():

    def __init__(self):
        self.description = str(subprocess.check_output("netsh wlan show interfaces"))

    def recognizeWifi(self):

        self.location = "Wifi Not Found or Unknow"
        
        for i in range(len(pastConnectionsKeys)):
            if pastConnectionsKeys[i] in self.description:
                self.location = pastConnections[pastConnectionsKeys[i]]

if __name__ == "__main__":

    test = ConnectedWifi()

    test.recognizeWifi()

    print(test.location)