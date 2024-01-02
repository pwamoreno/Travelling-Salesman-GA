import random

def Mutate(data):
    
    routes = data[0]
    
    rand1 = random.randint(0, len(routes) - 1)
    rand2 = random.randint(0, len(routes) - 1)

    routes[rand1], routes[rand2] = routes[rand2], routes[rand1]

    return data

