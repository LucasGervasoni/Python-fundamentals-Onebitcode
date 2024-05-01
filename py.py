from functools import reduce

# map
renan = ['sisi', 'bibi', 'titi', 'carla']

def Renan(item):
    return item.upper()

print(list(map(Renan,renan)))

# filter
scores = [73, 20, 65, 19, 76, 100, 88]

def above_half(item):
    return item > 50

print(list(filter(above_half, scores)))

# zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers[::-1])))

# reduce
my_numbers = [5,4,3,2,1]
scores = [73, 20, 65, 19, 76, 100, 88]

def acumulador(acc, item):
    print(acc, item)
    return acc + item

print(reduce(acumulador, (my_numbers + scores)))