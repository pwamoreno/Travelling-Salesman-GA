import sys, random
from firstGenPopulation import firstGenPopulation
from Mutation import Mutate
from Selection import Selection
from Crossover import CrossOver
from fitnessFunc import Fitness
from utils import *

from firstGenPopulation import firstGenPopulation


def GA(cityList, popSize, distances, Iterations):

    population = firstGenPopulation(cityList, popSize)

    res = int(sys.maxsize)
    nextGen = []
    i = 0

    while i < Iterations:
        population = Fitness(population=population, distances=distances)

        population.sort(key = lambda x: x[1])

        fittest = list.copy(population[0])

        if fittest[1] < res:
            result = list.copy(fittest)
            res = fittest[1]
            print("\n The solution is -" + str(i))
            print(result)

        while len(nextGen) < len(population):
            data1 = Selection(population)
            data2 = Selection(population)

            cross = CrossOver(data1, data2)

            offspring1 = Mutate(cross[0])
            offspring2 = Mutate(cross[1])

            nextGen.append(offspring1)
            nextGen.append(offspring2)

        population = nextGen
        nextGen = []
        i += 1

    print("Final Solution after " + str(i) +  " iterations = ")
    print(result)

    return result

distances = generateDistance(5, 20)

GA(5, 40, distances, 1000)