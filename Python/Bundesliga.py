#Say hello!
print ("Welcome to Bundesliga team & airport finder!")

teamArray = []
#print (teams)

# Club object
class Club:
    def __init__ (self, name, city, airport, stadium):
        self.name = name
        self.city = city
        self.airport = airport
        self.stadium = stadium 


    def printNearestAirport(self):
        print("---------------------")
        print("Club name: "+self.name)
        print("Nearest airport: "+self.airport)
        print("Stadium: " +self.stadium)
        
#Objects and array insert
bayern = Club("FC Bayern München", "München", "MUC", "Allianz Arena")
eintracht = (Club("Eintracht Frankfurt", "Frankfurt", "FRA", "Deutsche Bank Park"))
dortmund = (Club("Borussia Dortmund", "Dortmund", "DUS", "Signal Iduna Park"))
koln = Club("1. FC Köln","Köln", "DUS", "RheinEnergieStadion")
unionberlin = (Club("Union Berlin", "Berlin", "BER", "Alte Försterei"))
herthaberlin = (Club("Hertha Berlin", "Berlin", "BER", "Olympiastadion"))

teamArray.append(bayern)
teamArray.append(eintracht)
teamArray.append(dortmund)
teamArray.append(unionberlin)
teamArray.append(herthaberlin)



def printTeams(airportInput, teamArray):
    i = 0

    while(airportInput is not ""):
        for obj in teamArray:
           if obj.airport == airportInput:
              obj.printNearestAirport()
              i = i+1

        if i == 0:
            print("Airport not found!")
        print("Go again? (Y/N)")
        newJourneyInput = input()
        if(newJourneyInput is "Y"):
            print("Where do you want to travel (MUC, BER, DUS, FRA)?")
            airportInput=input()
        elif (newJourneyInput is "N"):
            airportInput=""
            print ("Gud spiel!")
        else:
            print ("Please answer Y or N!")
            exit


#Print club information
for obj in teamArray:
    obj.printNearestAirport()
    

print("Where do you want to travel (MUC, BER, DUS, FRA)?")
airportInput = input()
printTeams(airportInput, teamArray)
