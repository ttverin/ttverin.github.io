#from _typeshed import Self
import array
#Say hello! 
print ("Welcome to Bundesliga team & airport finder!")

teamArray = []
stadiumArray = []
#print (teams)

# Define Club object
class Club:
    def __init__ (self, name, city, airport, stadium):
        self.name = name
        self.city = city
        self.airport = airport
        self.stadium  = stadium

    #Define printNearestAirport 
    def printNearestAirport(self):
        print("---------------------")
        print("Club name: "+self.name)
        print("Nearest airport: "+self.airport)
        print("Stadium: " +self.stadium)

class Stadium:
    def __init__(self, name, city, capacity, beer):
        self.name = name
        self.city = city
        self.capacity = capacity
        self.beer = beer

    def printStadium(self):
        lessCapacity = self.capacity - 1
        print ("Stadium in "+self.city+": The name is "+self.name+", you will be supporting with "+str(lessCapacity)+" people and you will be drinking "+self.beer)
#Objects and array insert -- 
# These will later
# be read from a (XML) file with additional infromation such as links to ticket sales and schedule etc

bayern = Club("FC Bayern München", "München", "MUC", 'Allianz Arena')
achzehn = Club("1860 München", "München", "MUC", "Grunwalder Strasse")
eintracht = Club("Eintracht Frankfurt", "Frankfurt", "FRA", "Deutsche Bank Park")

dortmund = Club("Borussia Dortmund", "Dortmund", "DUS", "Signal Iduna Park")
koln = Club("1. FC Köln","Köln", "DUS", "Rheinenergiestadium")
fortuna = Club("Fortuna Dusseldorf", "Dusseldorf", "DUS","MerkurSpiel Arena")

unionberlin = Club("Union Berlin", "Berlin", "BER", "Alte Försterei")
herthaberlin = Club("Hertha Berlin", "Berlin", "BER", "Olympiastadion")

#Stadium objects
allianz = Stadium("Allianz Arena", "Munchen", 80000, "Paulaner")
rheinenergiestadion = Stadium("Rheinenergiestadin", "Köln", 50000,"Gaffel Kölsch")

#Insert team objects into an array
#tobe read from the file

teamArray.append(bayern)
teamArray.append(eintracht)
teamArray.append(dortmund)
teamArray.append(unionberlin)
teamArray.append(herthaberlin)
teamArray.append(achzehn)
teamArray.append(koln)
teamArray.append(fortuna)

stadiumArray.append(allianz)
stadiumArray.append(rheinenergiestadion)

#Cycle through the teams array and find the teams that match the airport input
def findStadium(airportInput, teamArray):
    while(airportInput):
        airportFound = 0
        for obj in teamArray:
           if obj.airport == airportInput:
              obj.printNearestAirport()
              airportFound = 1

        if airportFound == 0:
            print ("Airport not found!")
        
        print("Go again? (Y/N)")
        newJourneyInput = input()

        if(newJourneyInput == "Y"):
            print("Where do you want to travel (MUC, BER, DUS, FRA)?")
            airportInput=input()


        elif (newJourneyInput == "N"):
            print ("Gut spiel haben! Tschuss")
            airportInput=""
            exit

        else:
            print ("Please answer Y or N!")
            newJourneyInput=input()
            

def printStadiumInfos(stadiumInput, stadiumArray):
    for obj in stadiumArray:
        if obj.city == stadiumInput:
               obj.printStadium()


#Print club information
for obj in teamArray:
    obj.printNearestAirport()
    
#Print dialogue and ask for input, call for Flight/Stadium finder
#GUI will be added in the future
print("\nWhere do you want to travel (MUC, BER, DUS, FRA)?")
airportInput = input()
if airportInput == "":
    print("You didn't give a destination")
    print("Where do you want to travel (MUC, BER, DUS, FRA)?")
    airportInput=input()


#Call for findStadium mehtod to start the application
#findStadium(airportInput, teamArray)

printStadiumInfos(airportInput, stadiumArray)