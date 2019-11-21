import population, fitness, selection, crossover, mutation, maxmin

mutationRate = 0.003
crossoverRate = 0.3


size = 500
fileMax = open("valuesMax.txt","w")
fileMin = open("valuesMin.txt","w")
fileMed = open("valuesMed.txt","w")


# print("\n### INITIAL POPULATION ###\n")
currentPopulation = population.createPopulation(size)
# print(currentPopulation)
# print()

for i in range(100):
    # input()
    # print()
    # print("\n### POPULATION FITNESS ###")
    currentPopulation = fitness.calculatePopulationFitness(currentPopulation, size)
    # print()
    # print(currentPopulation)


    # print()
    # print("\n### CALCULATE MAX MIN ###")
    max = maxmin.calculateMax(currentPopulation)
    min = maxmin.calculateMin(currentPopulation)
    med = maxmin.calculateMed(currentPopulation, size)
    fileMax.write(str(i) + ', ' + str(max) + '\n')
    fileMin.write(str(i) + ', ' + str(min) + '\n')
    fileMed.write(str(i) + ', ' + str(med) + '\n')
    # print('Max value: ' + str(max))
    # print('Med value: ' + str(med))
    # print('Min value: ' + str(min))

    # ROLETA
    # print()
    currentPopulation = selection.rouletteSelection(currentPopulation, size)

    # print()

    currentPopulation = crossover.crossover(currentPopulation, size, crossoverRate)
    # print("\n### POPULATION AFTER CROSSOVER ###")
    # print(currentPopulation)

    # print()
    currentPopulation = mutation.mutate(currentPopulation, size, mutationRate)
    # print("\n### POPULATION AFTER MUTATION ###")
    # print(currentPopulation)

    # print()
    # print('### MAX and MIN values ###')
    # print('Max value: ' + str(max))
    # print('Med value: ' + str(med))
    # print('Min value: ' + str(min))


print("\n### POPULATION FITNESS ###")
currentPopulation = fitness.calculatePopulationFitness(currentPopulation, size)
print()
print(currentPopulation)


print()
print("\n### CALCULATE MAX MIN ###")
max = maxmin.calculateMax(currentPopulation)
min = maxmin.calculateMin(currentPopulation)
med = maxmin.calculateMed(currentPopulation, size)
fileMax.write(str(i) + ', ' + str(max) + '\n')
fileMin.write(str(i) + ', ' + str(min) + '\n')
fileMed.write(str(i) + ', ' + str(med) + '\n')
print('Max value: ' + str(max))
print('Med value: ' + str(med))
print('Min value: ' + str(min))


fileMax.close()
fileMin.close()
fileMed.close()