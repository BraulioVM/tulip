from itertools import product

def coordinates(size):
    i, j = size
    return product(range(i), range(j))
