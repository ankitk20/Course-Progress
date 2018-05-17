import random
import copy

with open('input', 'r') as file:
    conn = file.readlines()

graph = {}    
for line in conn:
  l = list(map(lambda x: int(x), line.strip().split('\t')))
  graph[l[0]] = l[1:]

# graph = {1:[2, 3, 4, 7], 2:[1, 3, 4], 3:[1, 2, 4], 4:[3, 1, 2, 5], 5:[4, 6, 7, 8], 6:[5, 7, 8], 7:[1, 5, 6, 8], 8:[5, 6, 7]}
# g = {1:[2, 3, 4, 7], 2:[1, 3, 4], 3:[1, 2, 4], 4:[3, 1, 2, 5], 5:[4, 6, 7, 8], 6:[5, 7, 8], 7:[1, 5, 6, 8], 8:[5, 6, 7]}
# graph = {1:[2, 3, 4], 2:[1, 3, 4, 5], 3:[1, 2], 4:[1, 2, 5], 5:[2, 4], 6:[1, 2, 4]}
# graph = {1:[3, 6], 2:[4, 6], 3:[1, 4, 5], 4:[2, 3], 5:[3, 6], 6:[1, 2, 5]}
# graph = {0:[1, 2, 3], 1:[0, 3], 2:[0, 3], 3:[0, 1, 2]}

def update_graph(edge, val):
  for key in graph.keys():
    neighbors = graph[key]
    i = 0
    while i < len(neighbors):
      if neighbors[i] in edge and key == val:							# removing self loops
        neighbors.pop(i)
        continue
      elif neighbors[i] in edge:													# updating old nodes with new node
        neighbors[i] = val
      i += 1

def main():
	global graph
	cut = 19900																							# max possible edges
	g = copy.deepcopy(graph)
	for it in range(100):
		graph = copy.deepcopy(g)
		new_edge = len(graph.keys()) + 1
		while len(graph.keys()) > 2:
			edge = random.choices(list(graph.keys()), k=2)
			if edge[0] == edge[1]:
				continue
			graph[new_edge] = graph[edge[0]] + graph[edge[1]]		# merging by combining neighbours
			del graph[edge[0]]
			del graph[edge[1]]
			update_graph(edge, new_edge)
			new_edge += 1
		c = max(len(graph[key]) for key in graph.keys())
		cut = c if cut > c else cut														# updating cut val if smaller cut found
		print(it+1)
	print(graph, cut)

main()


# 17
# 21
# 22
# 31
# 71