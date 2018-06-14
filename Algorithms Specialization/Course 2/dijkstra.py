from collections import defaultdict

with open('dijkstraData.txt', 'r') as file:
  f = file.readlines()

graph = defaultdict(lambda: defaultdict(int))
for line in f:
  c = line.split()
  key = int(c[0])
  conn = list(map(lambda x: tuple(map(int, x.split(','))), c[1:]))
  for c in conn:
    graph[key][c[0]] = c[1]

# graph = {1:{2:5, 4:9, 5:2}, 2:{1:5, 3:2}, 3:{2:2, 4:3}, 4:{1:9, 3:3, 6:2}, 5:{1:2, 6:3}, 6:{4:2, 5:3}}
parentof = defaultdict(int)
costof = defaultdict(int)
heapmap = dict()
for key in list(graph.keys()):
	heapmap[key] = 1000000


def shortestpath(current):
	global graph, parentof, costof, heapmap
	if not bool(heapmap):
		return
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
	shortestpath(current)


def main():
	global graph, parentof, costof, heapmap
	current = 1
	costof[current] = 0
	del heapmap[current]
	shortestpath(current)
	print(heapmap)
	# print(parentof)
	target = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
	for t in target:
		print(costof[t], end=',')

main()