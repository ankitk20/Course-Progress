import sys
import threading
import numpy as np
from itertools import combinations as comb
from collections import defaultdict
from math import floor

with open('tsp.txt', 'r') as file:
    f = file.readlines()
noofcities = int(f.pop(0))
coord = list()
for line in f:
    point = tuple(map(float, line.split()))
    coord.append(point)

distmatrix = np.zeros(shape=(noofcities, noofcities), dtype=float)

for i in range(noofcities):
    for j in range(i + 1, len(coord)):
        dist = ((coord[j][0] - coord[i][0]) ** 2 + (coord[j][1] - coord[i][1]) ** 2) ** 0.5
        distmatrix[i][j] = distmatrix[j][i] = dist

# distmatrix = [[0, 2, 9, 10],
#               [1, 0, 6, 4],
#               [15, 7, 0, 8],
#               [6, 3, 12, 0]]
# noofcities = 4

solvedproblems = defaultdict(lambda: defaultdict(int))
for i in range(2, noofcities + 1):
    solvedproblems[i][()] = distmatrix[i - 1][0]
# print(solvedproblems)

def mintravel(subset, exclude):
    global solvedproblems, distmatrix
    subset = set(subset)
    cost = min(distmatrix[exclude - 1][s - 1] + solvedproblems[s][tuple(subset - {s})] for s in subset)
    # print(subset, cost)
    return cost

def travel(noofcities, source=1):
    global solvedsubproblems
    cities = set(range(2, noofcities + 1))

    for i in range(1, noofcities):
        print(i)
        for c in comb(cities, i):
            for j in range(2, noofcities + 1):
                subset = tuple(set(c) - {j})
                if len(subset) >= i:
                    # print(j, subset, end='\t')
                    solvedproblems[j][subset] = mintravel(subset, j)

    # print(solvedproblems.items())
    return mintravel(cities, source)


def main():
    global noofcities
    result = travel(noofcities)
    print(floor(result))


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(800000)
    thread = threading.Thread(target=main)
    thread.start()