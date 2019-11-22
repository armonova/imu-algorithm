import random, population, maxmin, mutation

def rouletteSelection(population, size):
      randomNumbers = getRandomNumbers(population, size)
      # print("\n\n### RANDOM NUMBERS ###")
      # print(randomNumbers)
      selectedFathers = getSelectedFathers(population, randomNumbers, size)
      # print("\n\n### SELECTED FATHERS ###")
      # print(selectedFathers)
      return selectedFathers

def getRandomNumbers(population, size):
      maxValue = round(population[size - 1][3])
      # print(maxValue)
      randomGenerated = [0 for x in range(size)]
      for i in range(size):
            randomGenerated[i] = random.randint(0, maxValue)
      return randomGenerated

def getSelectedFathers(population, randomNumbers, size):
      selectedFathers = [[0 for x in range(4)] for y in range(size)]
      for i in range(size):
            randNumber = randomNumbers[i]
            # print("randNumber: " + str(randNumber))
            for j in range(size):
                  # print("\tj: " + str(j) + "\tpopulation[" + str(j) + "][3]: " + str(population[j][3]))
                  if(population[j][3] >= randNumber):
                        # print("\tselected " + str(population[j]))
                        selectedFathers[i] = population[j]
                        break
      
      return selectedFathers

def getSelectedFromCloneFathers(population, size, clonesCount):
      selectedFathers = []
      i = 0
      while(i < size):
            max = population[i][2]
            selected = population[i]
            for j in range(clonesCount):
                  if (population[i + j][2] > max):
                        max = population[i + j][2]
                        selected = population[i + j]

            i = i + clonesCount
            selectedFathers.append(selected)

      return selectedFathers

# size = 5
# pop = population.createPopulation(size)
# print("## CURRENT POPULATION ##")
# print(pop)
# print()

# newPop = population.clonePopulation(pop, size, 2)
# print("## CLONED POPULATION ##")
# print(newPop)

# newPop = getSelectedCloneFathers(newPop, size * 2, 2)
# print("## SELECTED POPULATION ##")
# print(newPop)