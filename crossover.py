import fitness, random

# alpha = número aleatório entre 0 e 1, diferente pra cada casal

def makeCrossover(father1, father2):
      son1 = [0 for x in range(4)]
      son2 = [0 for x in range(4)]

      alpha = round(random.uniform(0, 1), 1)
      # print("alfa: " + str(alpha))
      son1[0] = round((alpha * father1[0]) + ((1 - alpha) * father2[0]), 4)
      son1[1] = round((alpha * father1[1]) + ((1 - alpha) * father2[1]), 4)

      son2[0] = round((alpha * father2[0]) + ((1 - alpha) * father1[0]), 4)
      son2[1] = round((alpha * father2[1]) + ((1 - alpha) * father1[1]), 4)
      
      return son1, son2


def crossover(fathers, size, rate):
      i = 0
      while(i < size):
            rand = round(random.uniform(0, 1), 4)
            j = i + 1
            # print("i: " + str(i) + "  j: " + str(j) + "\trand: " + str(rand))
            if(j >= size):
                  break
            if(rand < rate):
                  # print("\tfathers  " + str(fathers[i]) + "  and  " + str(fathers[j]))
                  fathers[i], fathers[j] = makeCrossover(fathers[i], fathers[j])
                  # print("\tsons     " + str(fathers[i]) + "  and  " + str(fathers[j]))
            i = j + 1
      return fathers




# faz a roleta pra pegar quais os genes que vao cruzar;
      #
# para cada casal selecionado, usa a taxa de cruzamento pra ver se vai cruzar;

# se for cruzar:
      # cruzamento
            # x1filho1 = (alpha * x1pai1) + ((1 - alpha) * x1pai2)
            # x1filho2 = (alpha * x1pai2) + ((1 - alpha) * x1pai1)
            # x2 faz igual o x1
# se não
      # repete o casal


# depois do cruzamento, usa a taxa de mutação para ver se vai mutar PRA X1 E PRA X2 SEPARADO
# se for mutar:
      # muta
# se não for:
      # não muta