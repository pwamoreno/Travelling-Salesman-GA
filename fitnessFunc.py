from utils import getDistance

def Fitness(population, distances):

    for route in population:

        cost = 0
        searchedList = []

        for x in route[0]:
            for y in route[0]:

                if (x, y) in searchedList or (y, x) in searchedList:
                    continue

                cost += getDistance(x, y, distances) * getDistance(route[0][x], route[0][y], distances)

                searchedList.append((x, y))

        route[1] = cost


    return population

# Fitness([[[2, 0, 3, 4, 1], 0], [[1, 4, 2, 3, 0], 0], [[1, 2, 0, 3, 4], 0], [[1, 0, 3, 2, 4], 0], [[1, 3, 2, 0, 4], 0], [[1, 2, 4, 3, 0], 0], [[3, 0, 2, 1, 4], 0], [[3, 0, 2, 4, 1], 0], [[2, 1, 3, 0, 4], 0], [[2, 1, 0, 3, 4], 0]], {(0, 0): 0, (0, 1): 4, (0, 2): 4, (0, 3): 1, (0, 4): 5, (1, 1): 0, (1, 2): 16, (1, 3): 16, (1, 4): 5, (2, 2): 0, (2, 3): 3, (2, 4): 12, (3, 3): 0, (3, 4): 13, (4, 4): 0})