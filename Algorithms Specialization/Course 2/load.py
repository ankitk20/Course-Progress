import pickle as pk
from itertools import groupby
from collections import defaultdict

with open('SCC.txt', 'r') as file:
  f = file.readlines()
conn = [list(map(int, string.split())) for string in f]
conn_rev = [c[::-1] for c in conn]

# print(conn[:10])
# print(conn_rev[:10])

graph = defaultdict(list)
graph_rev = defaultdict(list)

g = groupby(conn, key=lambda x:x[0])
g_rev = groupby(conn_rev, key=lambda x:x[0])
for i in g:
	l = list(i[1])
	graph[i[0]] = list(map(lambda x: x[1], l))

for i in g_rev:
	l = list(i[1])
	graph_rev[i[0]] = list(map(lambda x: x[1], l))

with open('graph', 'wb') as f:
	pk.dump(graph, f)

with open('graph_rev', 'wb') as f:
	pk.dump(graph_rev, f)