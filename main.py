from algorithms.hillclimbing import hillclimbing
from algorithms.HcModified import hillclimbingModified
from excelExport import excelExport
from tsp import tsp
import numpy as np
import matplotlib.pyplot as plt
import time
#Data from: https://people.sc.fsu.edu/~jburkardt/datasets/cities/cities.html
if __name__ == '__main__':
    maxRepetitions = 31
    maxIterations = 1000
    directory = 'C:\\Users\\\DanielT\\Documents\\9no' \
                '\\Metaheuristica\\discreto-tsp\\problems\\'
    myProblem = tsp(directory + 'ulysses16..txt')
    myProblem2 = tsp(directory + 'att48..txt')
    myProblem3 = tsp(directory + 'att532..txt')
    myProblem4 = tsp(directory + 'bays29..txt')
    myProblem5 = tsp(directory + 'dantzig42..txt')

    myProblems = [myProblem,myProblem2,myProblem3,myProblem4,myProblem5]
    best = np.zeros(maxRepetitions, dtype=float)
    avgX = np.arange(0, maxIterations)
    myHC = hillclimbing(maxIterations)
    myHCM = hillclimbingModified(maxIterations)
    myAlgorithms = [myHC,myHCM]
    myLeg = []
    myData = []
    for problem in myProblems:
        for algorithm in myAlgorithms:
            avgY = np.arange(0, maxIterations)
            times = time.time()
            for i in range(maxRepetitions):
                np.random.seed(i)
                [x, y] = algorithm.evolve(problem)
                best[i] = algorithm.best.fitness
                avgY = avgY + y
            fin = time.time()
            times = fin - times
            avgY = avgY / maxRepetitions
            plt.plot(avgX, avgY)
            myLeg.append(str(algorithm))
            myData.append([problem.name, best.mean(), best.std(), best.max(), best.min(), times])
        # plotting
        plt.title("Convergence curve "+problem.name)
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.legend(myLeg)
        plt.show()
    myExport = excelExport(myData)
    myExport.evaluate()

    #print('AVG = ', best.mean(), ' +/- ', best.std(), ' MAX = ', best.max(), ' MIN =  ', best.min())

    # plotting
#    avgY = avgY / maxRepetitions
 #   avgY1 = avgY1 / maxRepetitions
    #fig1, ax1 = plt.subplots()
    #ax1.set_title('Box Plot for best solutions')
    #ax1.boxplot(best)
    #plt.show()