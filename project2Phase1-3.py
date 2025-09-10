#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:43:51 2024

@author: sriram
"""

# CS1210: Project 2 Phase 1 [5 functions to complete]
###############################################################################
# Complete the signed() function, certifying that:
# 1) the code below is entirely your work, and
# 2) it has not been shared with anyone outside the instructional team.
#
# ToDo: Change the words "hawkid" between the two double quote marks
# to match your own hawkid. Your hawkid is the "login identifier" you use
# to login to all University services, like `https://myUI.uiowa.edu/'
#
#
# Note: we are not asking for your password, just the login
# identifiers: for example, mine is "sriram".
#
###############################################################################
def signed():
    return(["lregehr"])

###############################################################################
#
# Specification: Reads information from the files "miles.txt" and loads all the 
# data from the file into a giant dictionary and returns this dictionary. The 
# organization of this dictionary has been specified in detail in the Project 2 handout. 
# If, for some reason, "miles.txt" is missing, your function should gracefully
# finish, returning the empty dictionary {}.
# 
###############################################################################
def loadData():
    CityDataDict= {}
    DistDict = {}
    try:
        f = open("miles.txt", "r") 
    except:
        return {}
    cityList = []
    cityData = []
    previousCities = []
    distAcc = []
    for line in f:
        if ("A" <= line[0]) and (line[0] <= "Z"):
            i = 0
            while (line[i] != ","):
                i = i + 1
            cityName = line[:i] + " " + line[i+2:i+4]
            previousCities.append(cityName)
            cityData = line[i+4:].split("]")[0][1:]
            population= line[i+4:].split("]")[1].strip()
            coord = cityData.split(",")
            for i in range(len(coord)):
                coord[i] = int(coord[i])
            cityData2 = [coord, int(population)]
            
            distAcc = []
            CityDataDict[cityName]= [coord, int(population), DistDict]
            DistDict = {}
        elif line[0].isdigit():
            distList = line.split()
            distAcc = distAcc + distList
            for i in range(len(distAcc)):
                DistDict[previousCities[i]]= int(distAcc[-1-i])
            CityDataDict[cityName]= [coord, int(population), DistDict]
    allCities = previousCities
    for i in range(len(allCities)):
        for j in range(i+1 ,len(allCities)):
            CityDistDict = CityDataDict[allCities[j]][2]
            Dist = CityDistDict[allCities[i]]
            CityIDistDict = CityDataDict[allCities[i]][2]
            CityIDistDict[allCities[j]] = Dist
        

    return CityDataDict
        
        
    
            
            

         
###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and a particular city name and returns the coordinates (which is a 
# list of 2 integers) of the given city. If, for some reason, cityName is not a key
# in cityDataDict, it returns None.
#
###############################################################################
def getCoordinates(cityDataDict, cityName):
    try:
        for i in range(len(cityDataDict[cityName][0])):
            cityDataDict[cityName][0][i] = int(cityDataDict[cityName][0][i])
        return cityDataDict[cityName][0]
    except:
        return None  
    
###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and a particular city name and returns the population (which is a 
# positive integer) of the given city. If, for some reason, cityName is not a key
# in cityDataDict, it returns None.
#
###############################################################################
def getPopulation(cityDataDict, cityName):
    try:
        return int(cityDataDict[cityName][1])
    except:
        return None 

###############################################################################
#
# Specification: takes the dictionary that contains all the information associated 
# with the cities and two city names and returns the distance (an integer) 
# between cities cityName1 and cityName2. If cityName1 and cityName2 are identical, 
# it returns 0. If either cityName1 or cityName2 are not in cityDataDict, it returns
# None.
#
###############################################################################    
def getDistance(cityDataDict, cityName1, cityName2):
    try:
        if cityName1 == cityName2 and cityName1 in cityDataDict and cityName2 in cityDataDict:
            return 0
        return int(cityDataDict[cityName1][2][cityName2])
    except:
        return None

###############################################################################
#
# Specification: The function takes 3 paramaters:
#    
# cityDataDict: the dictionary that contains all the information associated 
# with the cities
# 
# cityName: is a name of a city
#
# r: is a non-negative floating point number
#
# The function returns a list of cities at distance at most r from the given city,
# cityName. This list can contain the names of cities in any order. If cityName is
# not a key in cityDataDict, the function should return None.
#
###############################################################################
def nearbyCities(cityDataDict, cityName, r):
    nearByCities= [cityName]
    try:
        Cities = cityDataDict[cityName][2].keys()
        for city in Cities:
            if int(cityDataDict[cityName][2][city]) <= r:
                nearByCities.append(city)
    except:
        return None
    return nearByCities
