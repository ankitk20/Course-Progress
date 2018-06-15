with open('clustering1.txt') as file:
	lines = file.readlines()

edges = list(map(lambda edge: tuple(map(int, edge.split())), lines))
nodecount = edges.pop(0)[0]

cluster = dict()
cost = dict()

for i in range(1, 5):
	cluster[i] = set()

edges.sort(key=lambda x:x[2])
vertices = {}
for edge in edges:
    vertices[edge[0]] = edge[0]
    vertices[edge[1]] = edge[1]

for vertex in vertices:
    cost[vertex] = 0

clustercount = len(vertices)

for edge in edges:
    head1 = vertices[edge[0]]
    while vertices[head1] != head1:
        head1 = vertices[head1] 

    head2 = vertices[edge[1]]
    while vertices[head2] != head2:
        head2 = vertices[head2] 

    if head1 != head2:
        if clustercount == 4:
            spacing = edge[2]
            break
        vertices[head2] = head1
        cost[head1] += (edge[2] + cost[head2])
        clustercount -= 1

print(spacing)