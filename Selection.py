import random

def Selection(population):

    newList = random.sample(population, int(len(population)/5))

    newList.sort(key = lambda x: x[1])

    return newList[0] 

# Selection([[[2, 0, 3, 4, 1], 532], [[1, 4, 2, 3, 0], 615], [[1, 2, 0, 3, 4], 525], [[1, 0, 3, 2, 4], 547], [[1, 3, 2, 0, 4], 507], [[1, 2, 4, 3, 0], 492], [[3, 0, 2, 1, 4], 507], [[3, 0, 2, 4, 1], 566], [[2, 1, 3, 0, 4], 709], [[2, 1, 0, 
# 3, 4], 720]])