import random

def firstGenPopulation(cityList, popSize):
    population = []

    for i in range(popSize):
        route = random.sample(range(cityList), cityList)
        population.append([route, 0])

    return population

# firstGenPopulation(5, 10)