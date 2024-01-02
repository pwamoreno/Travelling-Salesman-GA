import random
from duplicates import duplicates


def CrossOver(data1, data2):

    data1[1] = 0
    data2[1] = 0

    route1 = list.copy(data1[0])
    route2 = list.copy(data2[0])
    

    for i in range(len(route1)):
        prob = random.randrange(2)
        if prob == 0:
            route1[i], route2[i] = route2[i], route1[i]

    dupInRoute1 = list(duplicates(route1))
    dupInRoute2 = list(duplicates(route2))

    for i in dupInRoute1:
        if i in route1:
            route2.append(i)

    

    for i in dupInRoute2:
        if i in route2:
            route1.append(i)


    data1[0] = route1
    data2[0] = route2




    return [data1, data2]
    # print(data1)
    # print(data2)

    # print(route1)
    # print(route2)

    
    # dup1 = []
    # for i in route1:
    #     if route1.count(i) > 1:
    #         dup1.append(i)
    # print(dup1)

    # dup2 = []
    # for i in route2:
    #     if route2.count(i) > 1:
    #         dup2.append(i)
    # print(dup2)

    # for i in dup1:
    #     if i in route1:
    #         route1.remove(i)
    #         route2.append(i)
    
    # for i in dup2:
    #     if i in route2:
    #         route2.remove(i)
    #         route1.append(i)

    # print(route1)
    # print(route2)
    # print(dupInRoute1)

    



    # data1[0] = route1
    # data2[0] = route2

    # print(data1)
    # print(data2)
 
    # print(list(dupInRoute1))
    # print(list(dupInRoute2))


# CrossOver([[1, 2, 4, 3, 0], 492],[[3, 0, 2, 1, 4], 507])