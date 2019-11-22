import random

def createPopulation(size):
    '''Returns a matrix of the following size. Each line is as follows [x1, x2, fitness, Σfitness]'''
    population = [[0 for x in range(4)] for y in range(size)]

    for i in range(size):
        population[i][0] = round(random.uniform(0, 10), 4)
        population[i][1] = round(random.uniform(0, 10), 4)
    # print(population)
    return population


def clonePopulation(population, size, clonesCount):
      selectedFathers = []
      for i in range(size):
            for j in range(clonesCount):
                  selectedFathers.append(population[i])

      return selectedFathers

size = 5
pop = createPopulation(size)
print(pop)
print()
newPop = clonePopulation(pop, size, 2)
print(newPop)