import numpy as np
from tsp import tsp


class solution:
    def __init__(self, p: tsp):
        self.problem = p
        self.cells = []
        self.fitness = 0.0

    def from_solution(self, origin):
        self.problem = origin.problem
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness

    def randomInitialization(self):
        #self.cells = np.arange(self.problem.size)
        self.cells = np.zeros(self.problem.size, dtype=int)
        self.cells = (np.random.choice(self.problem.size, self.problem.size, replace=False))
        self.fitness = self.problem.evaluate(self.cells)

    def randomInitializationVariation(self):
        self.cells = []
        #self.cells = np.arange(self.problem.size)
        cellsAux = np.random.choice(self.problem.size, self.problem.size, replace=False)
        for i in range(0,self.problem.size,2):
            self.cells.append(np.random.choice(cellsAux))
            position,cellsAux = self.__withBestDistance([cellsAux,i])
            self.cells.append(position)
            if i+2 > self.problem.size:
                break
        self.fitness = self.problem.evaluate(self.cells)

    def __withBestDistance(self,parms):
        cellsAux,pos = parms
        cellsAux[np.where(cellsAux == self.cells[pos])]=-1
        arreglo = np.delete(self.problem.distances[self.cells[pos]],self.cells)
        min = arreglo.min()
        index = np.where(self.problem.distances[self.cells[pos]] == min)[0][0]
        cellsAux[index]=-1
        return index, cellsAux

    def tweak(self):
        #print(self.cells, ' fitness = ', self.fitness)
        pos = np.random.choice(np.arange(1, self.problem.size), 2, replace=False)
        pos.sort()
        i = pos[0]
        k = pos[1]
        self.cells[i:k] = self.cells[k-1:i-1:-1]
        self.fitness = self.problem.evaluate(self.cells)
        #print(self.cells, ' fitness = ', self.fitness)

    def tweakVariation(self):
        #print(self.cells, ' fitness = ', self.fitness)
        pos = np.random.choice(np.arange(1, self.problem.size), 3, replace=False)
        pos.sort()
        i = pos[0]
        k = pos[1]
        j = pos[2]

        self.cells[i:k] = self.cells[k-1:i-1:-1]
        self.cells[k:j] = self.cells[j - 1:k - 1:-1]
        self.fitness = self.problem.evaluate(self.cells)
        #print(self.cells, ' fitness = ', self.fitness)

    def show(self):
        print(self.cells)
        print(self.fitness)