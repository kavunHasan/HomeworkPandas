import csv
def main():
    try:

        the_list = []
        city = []
        lats = []
        lngs = []
        fileName = input("Enter an input filename: ")
        data = open(fileName,"r")
        #taking everything from .csv file to a list
        for i in data:
            row = i.strip().split(",")
            the_list.append(row)
        #deleting first item of the list because it's headers
        del the_list[0]
        #taking city names from the list
        for i in the_list:
            city.append(i[0])
        #taking lat values from the list
        for i in the_list:
            lats.append(i[1])
        #taking lng values from the list
        for i in the_list:
            lngs.append(i[2])
        #finding capital and declare
        for i in the_list:
            if i[6] == "capital":
                capital_city = i[0]
        #functions that finds the mosts
        def mostEasternCity():
            max_lng = max(lngs) #max value of the lngs's values
            for i,j in zip(city,lngs): #finding whose value's is the max one
                if j == max_lng:
                    mostEasternCity = i
            return mostEasternCity #return the city name of max value
        def mostWesternCity():
            min_lng = min(lngs)
            for i,j in zip(city,lngs):
                if j == min_lng:
                    mostWesternCity = i
            return mostWesternCity
        def mostNorthernCity():
            max_lat = max(lats)
            for i,j in zip(city,lats):
                if j == max_lat:
                    mostNorthernCity = i
            return mostNorthernCity
        def mostSouthernCity():
            min_lat = min(lats)
            for i,j in zip(city,lats):
                if j == min_lat:
                    mostSouthernCity = i
            return mostSouthernCity
        #outputs
        print("Capital city:",capital_city) 
        print("Most eastern city:",mostEasternCity())
        print("Most western city:",mostWesternCity())
        print("Most northern city:",mostNorthernCity())
        print("Most southern city:",mostSouthernCity(),"\n")

        headers = ["Administrative City", "Number of Its Cities/Towns", "Total Population"]
        admincities = []
        numberOfCities = []
        totalPopulation = []
        #taking all admin cities from the list
        for i in the_list:
            if i[6] != "minor":
                admincities.append(i[0])
        #taking and counting Number of Its Cities/Towns from the list
        for i in the_list:
            countOfCities = 0
            for j in the_list:
                if i[0] == j[5]:
                    countOfCities += 1
            if i[6] != "minor":
                numberOfCities.append(str(countOfCities))
        #taking and calculating Total Population from the list
        for i in the_list:
            totalpop = 0
            for j in the_list:
                if i[0] == j[5] and j[7] != "":
                    totalpop += int(j[7])
            if i[6] != "minor":
                totalPopulation.append(str(totalpop))
        #creating dictionary that holds admin names as key and number of cities and total pop list as value
        miniDict = dict()
        for i in range(len(admincities)):
            miniDict[admincities[i]] = list()
            miniDict[admincities[i]].append(numberOfCities[i])
            miniDict[admincities[i]].append(totalPopulation[i])
        #writing dictionary we just created to a .csv file
        def saveCities():
            outputFileName = input("Enter an output filename: ")
            outputFile = open(outputFileName, "w")
            outputFile.write(headers[0] + "," + headers[1] +"," +headers[2] + "\n")
            for key in miniDict.keys():
                outputFile.write(key + "," + miniDict[key][0] + "," + miniDict[key][1] + "\n")
            outputFile.close()
        
        saveCities()
    except:
        #output if something goes wrong about filename
        print(fileName,"does not exist")
      
main()