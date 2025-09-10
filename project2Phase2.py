from project2Phase1 import *


def greedyFacilitySet(cityDataDictionary, r):

    unservedCities = [city for city in cityDataDictionary.keys()]
    servedCities = set()
    facilityList = []
    count = 0
    
    while unservedCities != []:
        mostServedCity = ""
        mostServed = 0
        for city2 in unservedCities:
            count = 0
            for city3 in nearbyCities(cityDataDictionary, city2, r):
                if city3 not in servedCities:
                    count += 1
            citiesServed = count
            if citiesServed > mostServed:
                mostServed = citiesServed
                mostServedCity = city2
            if citiesServed == mostServed:
                mostServedCity = min(city2, mostServedCity)
        if mostServedCity == "":
            break
        facilityList.append(mostServedCity)
        unservedCities.remove(mostServedCity)
        closeCities = nearbyCities(cityDataDictionary, mostServedCity, r)
        for city1 in closeCities:
                if city1 not in servedCities:
                    servedCities.add(city1)
    
    return facilityList
def combinationsOfCities(keys, n):
    if n == 0:
        return [[]]
    combo = []
    for i in range(0, len(keys)):
        city = keys[i]
        remCity = keys[i + 1:]

        remCity_combo = combinationsOfCities(remCity, n-1)
        for c in remCity_combo:
            temp = [city]
            temp.extend(c)
            combo.append(temp)
    return combo
    


def optimalFacilitySet(cityDataDictionary, r, oneSolution):
     citiesAll = []
     numCitiesAll = []
     
     for n in range(len(oneSolution)):
         combos = combinationsOfCities([city for city in cityDataDictionary.keys()], n)
         for cityCombo in combos:
            totalCities = set()
            for city in cityCombo:
                nbc = set(nearbyCities(cityDataDictionary, city, r))
                for city2 in nbc:
                    totalCities.add(city2)
            if len(totalCities) < len(cityDataDictionary.keys()):
                continue
            else:
                return cityCombo
            
     return []

