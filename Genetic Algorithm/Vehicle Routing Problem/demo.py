import random
import math
import os
import time
import matplotlib.pyplot as plt
nodes = {
    0: (82, 76),
    1: (96, 44),
    2: (50, 5),
    3: (49, 8),
    4: (13, 7),
    5: (29, 89),
    6: (58, 30),
    7: (84, 39),
    8: (14, 24),
    9: (2, 39),
    10: (3, 82),
    11: (5, 10),
    12: (98, 52),
    13: (84, 25),
    14: (61, 59),
    15: (1, 65)
}

#best_way = [(82, 76), (61, 59), (84, 25), (84, 25), (58, 30), (49, 8), (49, 8), (13, 7), (14, 24), (50, 5), (50, 5), (84, 25), (84, 25), (84, 25), (84, 39), (84, 39), (82, 76)]

nAlle = len(nodes)
nKrom = 8
nGeneration = 30

pCross = 1
pMutasi = 0

# Print iterations progress


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def generateChromosome(nodes):
    index = [0] + random.sample(range(1, 16), 15) + [0]
    chromosome = [nodes[i] for i in index]
    return chromosome


def countFitness(chromosome):
    fit = 0.0
    for i in range(len(chromosome) - 1):
        fit += math.sqrt(((chromosome[i + 1][0] - chromosome[i][0])
                          ** 2) + ((chromosome[i + 1][1] - chromosome[i][1]) ** 2))
    return ((1 / fit) * 100)


def generatePopulation(nodes, nChrom):
    pop = []
    for i in range(nChrom):
        pop.append(generateChromosome(nodes))
    return pop


def randomParent(nChrom):
    return random.randint(0, nChrom)


if __name__ == '__main__':
    os.system("cls")
    printProgressBar(0, nGeneration, prefix = 'Progress:', suffix = 'Complete', length = 50)
    plt.ion()
    pop = generatePopulation(nodes, nKrom)
    for i in range(int(nGeneration)):
        anak = []
        fitness = []
        #print("Generasi ke-" + str(i))
        for j in range(int(nKrom / 2)):
            # SELEKSI ORANG TUA
            parent1 = randomParent(nKrom - 1)
            parent2 = randomParent(nKrom - 1)

            anak1 = pop[parent1][:]
            anak2 = pop[parent2][:]

            # CROSSOVER
            rand = random.random()
            del anak1[0]
            del anak1[-1]
            del anak2[0]
            del anak2[-1]
            titik = random.randint(0, len(anak1)-1)
            if (rand <= pCross):
                for k in range(titik):
                    anak1[k], anak2[k] = anak2[k], anak1[k]
            anak1.insert(0,nodes[0])
            anak1.append(nodes[0])
            anak2.insert(0,nodes[0])
            anak2.append(nodes[0])
            

            # MUTASI
            rand = random.random()
            titik1 = random.randint(1, nAlle-1)
            titik2 = random.randint(1, nAlle-1)
            if ((rand <= pMutasi) and (titik1 != 0) and (titik2 != 0) and (titik1 != titik2) and (titik1 != 16) and (titik2 != 16)):
                anak1[titik1], anak1[titik2] = anak1[titik2], anak1[titik1]

            rand = random.random()
            titik1 = random.randint(1, nAlle-1)
            titik2 = random.randint(1, nAlle-1)
            if ((rand <= pMutasi) and (titik1 != 0) and (titik2 != 0) and (titik1 != titik2) and (titik1 != 16) and (titik2 != 16)):
                anak2[titik1], anak2[titik2] = anak2[titik2], anak2[titik1]

            anak.append(anak1)
            anak.append(anak2)

        # PRINT ANAK
        gab = pop + anak
        for j in range(len(gab)):
            fitness.append(countFitness(gab[j]))

        # print(fitness)

        # PRINT STEADYSTATE
        steadyState = sorted(range(len(fitness)),
                             key=lambda k: fitness[k], reverse=True)
        # steadyState = fitness.sort()
        pop = []
        for j in range(nKrom):
            pop.append(gab[steadyState[j]])

        #print(pop, end='\n \n')
        x = []
        y = []
        for cor in pop[0]:
            x.append(cor[0])
            y.append(cor[1])
        plt.clf()
        plt.plot(x, y)
        printProgressBar(i + 1, nGeneration, prefix='Progress:',
                         suffix='Complete', length=50)
        plt.pause(0.05)

    print("Jalur terbaik:")
    print(pop[0])
    print("Fitness: " + str(fitness[0]))
    plt.clf()
    plt.plot(x, y)
    plt.pause(123)
