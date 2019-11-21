import random

def mutate(population, size, rate):
    for i in range(size):
        for j in range(2):
            rand = round(random.uniform(0, 1), 4)
            if(rand <= rate):
                population[i][j] = makeMutation(population[i][j], i, j)
    
    return population

def makeMutation(value, i, j):
    rand = round(random.uniform(-1, 1), 4)
    # print()
    # print("Index i: " + str(i) + " Index j: " + str(j))
    # print("mutated value: " + str(rand))
    # print("\told value: " + str(value))
    value = round((value + rand), 4) 
    if value < 0:
        value = 0
    if value > 10:
        value = 10
    # print("\tnew value: " + str(value))
    return value