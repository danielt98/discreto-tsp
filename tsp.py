import numpy as np
import ntpath


class tsp:
    def __init__(self, filename):
        file1 = open(filename, 'r')
        lines = file1.readlines()
        self.name=ntpath.basename(filename)

        self.size = int(lines[0])
        self.distances = np.zeros((self.size, self.size), dtype=float)

        x = np.zeros(self.size, float)
        y = np.zeros(self.size, float)
        positionLine = 1
        for i in range(0, self.size):
            line = lines[positionLine].split(' ')
            x[positionLine - 1] = float(line[0])
            y[positionLine - 1] = float(line[1])
            positionLine = positionLine + 1
        for i in range(0, self.size):
            for j in range(i + 1, self.size):
                dis = np.sqrt(np.square(x[i] - x[j]) + np.square(y[i] - y[j]))
                self.distances[i][j] = self.distances[j][i] = dis

    def evaluate(self, cells):
        fitness = 0
        for i in range(self.size):
            j = i + 1
            if j >= self.size:
                j = 0
            fitness = fitness + self.distances[cells[i]][cells[j]]
        return fitness
