with open('edges.txt', 'r') as file:
    lines = file.readlines()

edges = list(map(lambda edge: tuple(map(int, edge.split())), lines))
totalvertices, totaledges = edges[0][0], edges[0][1]
edges.pop(0)

vertices = set()
spannedvertex = set()

for edge in edges:
    # print(edge)
    vertices.add(edge[0])
    vertices.add(edge[1])
spannedvertex.add(vertices.pop())

totalcost = 0

while len(vertices) > 0:
    bestcost = 9999999
    for edge in edges:
        if edge[0] in spannedvertex and edge[1] in vertices and edge[2] < bestcost:
            bestcost = edge[2]
            bestvertex = edge[1]
        if edge[1] in spannedvertex and edge[0] in vertices and edge[2] < bestcost:
            bestcost = edge[2]
            bestvertex = edge[0]
    spannedvertex.add(bestvertex)
    vertices.remove(bestvertex)
    totalcost += bestcost

# print(vertices)
# print(spannedvertex)

print(totalcost)