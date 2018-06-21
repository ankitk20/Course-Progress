import sys
import threading
from math import floor

with open('nn.txt', 'r') as file:
    f = file.readlines()
noofcities = int(f.pop(0))
coord = list()
for line in f:
    point = tuple(map(float, line.split()[1:]))
    coord.append(point)

visited = dict()
start = current = 0

def distcalc(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def heuristictravel(current, approxcost, noofcities, source=0):
    global coord, visited
    print(len(visited))
    if current == source and current in visited:
        return approxcost

    visited[current] = True

    mincost = 10 ** 10
    flag = False
    for i in range(noofcities):
        if len(visited) == noofcities:
            flag = True
        if i == current or i in visited:
            continue
        else:
            dist = distcalc(coord[current], coord[i])
            if mincost > dist:
                mincost = dist
                nextcity = i
    if flag:
        nextcity = source
        mincost = distcalc(coord[current], coord[source])
    return heuristictravel(nextcity, approxcost + mincost, noofcities)

def main():
    global start, noofcities
    approxcost = heuristictravel(start, 0, noofcities)
    print(floor(approxcost))

if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(800000)
    thread = threading.Thread(target=main)
    thread.start()