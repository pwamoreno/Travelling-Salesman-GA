def duplicates(route):
    dup = []
    for i in route:
        if route.count(i) > 1:
            route.remove(i)
            dup.append(i)
    return dup
    # print(route)

# duplicates([3, 1, 0, 4, 4])
# duplicates([1, 0, 3, 2, 2])