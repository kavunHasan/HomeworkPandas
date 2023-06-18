#importing libraries
import csv
import pandas as pd
#main function
def main2():
    #try block for error handling
    try:
        #functions that finds the mosts
        def mostEasternCity():
            lngs = pd.DataFrame(data.lng)       #declaring object, "lngs" to 
            max_lng = lngs.max(axis=0).iloc[0]  #
            for i,j in zip(data.city,data.lng): #
                if j == max_lng:                #
                    mostEasternCity = i         #
            return mostEasternCity              #
        def mostWesternCity():
            lngs = pd.DataFrame(data.lng)
            min_lng = lngs.min(axis=0).iloc[0]
            for i,j in zip(data.city,data.lng):
                if j == min_lng:
                    mostWesternCity = i
            return mostWesternCity
        def mostNorthernCity():
            lats = pd.DataFrame(data.lat)
            max_lat = lats.max(axis=0).iloc[0]
            for i,j in zip(data.city,data.lat):
                if j == max_lat:
                    mostNorthernCity = i
            return mostNorthernCity
        def mostSouthernCity():
            lats = pd.DataFrame(data.lat)
            min_lat = lats.min(axis=0).iloc[0]
            for i,j in zip(data.city,data.lat):
                if j == min_lat:
                    mostSouthernCity = i
            return mostSouthernCity
        #fileName = input("Filename please: ")
        data = pd.read_csv("tr_cities.csv")
        major_city_lines = data[data["type"] != "minor"]
        
        capital_city = data[data["type"] == "capital"]
        capital_city_name = pd.DataFrame(capital_city.city)
        print("Capital city:", capital_city_name.at[1,"city"])
        print("Most eastern city:",mostEasternCity())
        print("Most western city:",mostWesternCity())
        print("Most northern city:",mostNorthernCity())
        print("Most southern city:",mostSouthernCity(),"\n")
        the_dict = dict()
        for i in major_city_lines.city:
            the_dict[i] = list()
            city_related_rows = data[data["admin_name"] == i]
            thepop = pd.DataFrame(city_related_rows.population)
            total_pop = thepop.sum(axis=0).iloc[0]
            the_dict.get(i).append(city_related_rows.shape[0])
            the_dict.get(i).append(total_pop)

        #outputFileName = input("Enter an output filename: ")
        print("Cities are saved")
        
        def saveCities():
            header = ["Administrative City", "Number of Its Cities/Towns", "Total Population"]
            outputFile = open("tr_blabla.csv","w", newline="")
            writer = csv.writer(outputFile)
            writer.writerow(header)
            writer.writerows(the_dict)
            for i in the_dict:
                writer.writerow([i])
            for i in the_dict:
                writer.writerow(the_dict[i])
            outputFile.close()
        
        
        saveCities()
        

    except:
        #print(fileName,"does not exist")
        pass

main2()
