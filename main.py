import population, fitness, selection, crossover, mutation, maxmin

mutationRate = 0.003
crossoverRate = 0.3

max_it = 50
N = 50
n1 = 50
n2 = 0
beta = 0.1
Nc = beta * N
p = 20

size = 500
fileMax = open("valuesMax.txt","w")
fileMin = open("valuesMin.txt","w")
fileMed = open("valuesMed.txt","w")


# print("\n### INITIAL POPULATION ###\n")
currentPopulation = population.createPopulation(size)
# print(currentPopulation)
# print()

for i in range(max_it):
    # 1. Gere um conjunto (P) de candidatos a solução, composto pelo subconjunto de células de 
    # memória (M) mais o restante (P{r}) da população (P = P{r}  M);
    currentPopulation = fitness.calculatePopulationFitness(currentPopulation, size)
    
    # 2. Determine (processo de seleção) os n melhores indivíduos (P{n})
    # da população (P), baseado em uma medida de afinidade;
    max = maxmin.calculateMax(currentPopulation)
    min = maxmin.calculateMin(currentPopulation)
    med = maxmin.calculateMed(currentPopulation, size)
    fileMax.write(str(i) + ', ' + str(max) + '\n')
    fileMin.write(str(i) + ', ' + str(min) + '\n')
    fileMed.write(str(i) + ', ' + str(med) + '\n')
    
    # 3. Reproduza (processo de clonagem) estes n melhores indivíduos,
    # gerando uma população temporária de clones (C). A quantidade
    # de filhos de cada indivíduo é diretamente proporcional à sua afinidade;
    currentPopulation = selection.rouletteSelection(currentPopulation, size)

    # 4. Submeta a população de clones a um esquema de
    # hipermutação, em que a taxa de mutação é inversamente
    # proporcional à afinidade do anticorpo. Uma população de
    # anticorpos maduros é gerada (C*);
    currentPopulation = mutation.hiperMutate(currentPopulation, size, max, p)

    
    # 5. Re-selecione os melhores indivíduos de C* para compor o
    # conjunto de memória M;
    currentPopulation = fitness.calculatePopulationFitness(currentPopulation, size)
    max = maxmin.calculateMax(currentPopulation)
    min = maxmin.calculateMin(currentPopulation)
    med = maxmin.calculateMed(currentPopulation, size)
    fileMax.write(str(i) + ', ' + str(max) + '\n')
    fileMin.write(str(i) + ', ' + str(min) + '\n')
    fileMed.write(str(i) + ', ' + str(med) + '\n')
    
    # 6. Substitua d anticorpos por novos indivíduos (diversidade). Os
    # anticorpos com menores afinidades possuem maiores
    # probabilidades de serem substituídos.
    # @TODO Substituir os anticorpos


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