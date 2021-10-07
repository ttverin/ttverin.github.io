import array
#Say hello!

print ("Welcome to Bundesliga team & airport finder!")

teamArray = []
teams = ['Köln', 'Fc Bayern', 'Fortuna Dusseldorf']
#print (teams)

# Club objects

class Club:
    def __init__ (self, name, city, airport, stadium):
        self.name = name
        self.city = city
        self.airport = airport
        self.stadium = stadium

    def printNearestAirport(self):
        print("Club name "+self.name)
        print("Nearest airport "+self.airport)

bayern = Club("FC Bayern München", "München", "MUC", "Allianz Arena")
eintracht = (Club("Eintracht Frankfurt", "Frankfurt", "FRA", "Deutsche Bank Park"))
dortmund = (Club("Borussia Dortmund", "Dortmund", "DUS", "Signal Iduna Park"))
unionberlin = (Club("Union Berlin", "Berlin", "BER", "Alte Försterei"))
herthaberlin = (Club("Hertha Berlin", "Berlin", "BER", "Olympiastadion"))

bayern.printNearestAirport()

teamArray.append(bayern)
teamArray.append(eintracht)
teamArray.append(dortmund)
teamArray.append(unionberlin)
teamArray.append(herthaberlin)


for obj in teamArray:
    obj.printNearestAirport()
    

