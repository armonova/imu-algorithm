import math


def calculateFitness(xVec):
    prod = 1
    for x in xVec:
        prod *= math.sqrt(x)*math.sin(x)
    prod += 7  # adding 7 so fitness will never be a negative value
    prod = round(prod, 4)
    return prod


def calculatePopulationFitness(population, size):
    fitnessSum = 0
    populationAux = []
    for i in range(size):
        populationAux.append([])
        populationAux[i].append(population[i][0])
        populationAux[i].append(population[i][1])
    # print(population)
    for i in range(size):
        fitness = calculateFitness([population[i][0], population[i][1]])
        fitnessSum += fitness
        populationAux[i].append(fitness)
        populationAux[i].append(fitnessSum)
    return populationAux