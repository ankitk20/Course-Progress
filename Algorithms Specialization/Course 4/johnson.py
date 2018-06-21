import sys
from collections import defaultdict

with open('g3.txt', 'r') as file:
  f = file.readlines()
graph = defaultdict(lambda: defaultdict(int))
f.pop(0)
for line in f:
  tail, head, weight = tuple(map(int, line.split()))
  graph[tail][head] = weight

# graph = {
#     1: {2: 4, 3: 9, 6: 14},
#     2: {1: 7, 3: -10, 4: 15},
#     3: {1: -9, 2: 10, 4: 11, 6: 2},
#     4: {2: 15, 3: -14, 5: 6},
#     5: {4: 6, 6: -19},
#     6: {1: 4, 3: -20, 5: 9}
# }
graph = defaultdict(dict, graph)
stdist = dict()
parentof = defaultdict(int)
costof = defaultdict(int)
heapmap = dict()
for key in list(graph.keys()):
	heapmap[key] = 10 ** 6			# equivalent to infinity

def dijkstra(current):
	global graph, parentof, costof, heapmap
	if not bool(heapmap):
		return
	# print(current)
	neighbours = tuple(graph[current].keys())
	# print('neighbours are ', neighbours)
	for n in neighbours:
		new_weight = costof[current] + graph[current][n]
		try:
			if new_weight < heapmap[n]:
				heapmap[n] = new_weight
				# costof[n] = new_weight
				parentof[n] = current
		except KeyError:
			continue

	current = sorted(heapmap, key=heapmap.get)[0]
	costof[current] = heapmap[current]
	del heapmap[current]
	dijkstra(current)

def reweight():
	global graph, stdist
	print('reweight started')
	for tail in list(graph.keys()):
		for head in graph[tail]:
			graph[tail][head] = weight + stdist[tail] - stdist[head]

	print('reweight terminated')

def bellmanford(source):
	global graph, stdist
	print('bellmanford started')
	stdist = {v:0 if v == source else 10 ** 6 for v in list(graph.keys())}
	for i in range(len(stdist)):
		print(i)
		for tail, edges in graph.items():
			for head in edges:
				if stdist[head] > stdist[tail] + graph[tail][head]:
					stdist[head] = stdist[tail] + graph[tail][head]
	
	for tail, edges in graph.items():
		for head in edges:
			if stdist[head] > stdist[tail] + graph[tail][head]:
				return True
	print('bellmanford terminated')
	return False

def johnson():
	global graph, stdist, heapmap, costof, parentof
	for vertex in list(graph.keys()):
		graph[0][vertex] = 0
	negativecycle = bellmanford(0)
	if negativecycle:
		return (False, None)
	reweight()
	print('dijkstra will start now')
	result = dict()
	del graph[0]
	for tail in list(graph.keys()):
		print('source as ', tail)
		costof[tail] = 0
		dijkstra(tail)
		result[tail] = {head:dist - stdist[tail] + stdist[head] for head, dist in costof.items()}

	return (not negativecycle, result)


if __name__ == '__main__':
	sys.setrecursionlimit(5000)
	negativecycle, result = johnson()
	min_cost = min(min(d.values()) for d in result.values())
	print(min_cost)