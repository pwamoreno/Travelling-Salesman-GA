import random

def generateDistance(size, upperBound):

    dictionary = {}
    for i in range(size):
        for j in range(size):

            if i == j:
                dictionary[i, j] = 0
            
            if (j, i) in dictionary:
                continue

            dictionary[i, j] = random.randrange(0, upperBound)

    return dictionary



def getDistance(i, j, dictionary):
    if (i, j) not in dictionary:
        return dictionary[j, i]
    
    return dictionary[i, j]



def routeCost(route, distances):
    searchedList = []
    cost = 0

    for x in route:
        for y in route:
            if (x, y) in searchedList or (y, x) in searchedList:
                continue

            cost += getDistance(x, y, distances) * getDistance(route[0][x], route[0][y], distances)

            searchedList.append((x, y))

    return cost