import sys, threading, pickle as pk
from queue import PriorityQueue
from collections import defaultdict
with open('graph', 'rb') as f:
	graph = pk.load(f)
with open('graph_rev', 'rb') as f:
	graph_rev = pk.load(f)

# graph = {1:[4], 2:[8], 3:[6], 4:[7], 5:[2], 6:[9], 7:[1], 8:[5, 6], 9:[3, 7]}
# graph_rev = {1:[7], 2:[5], 3:[9], 4:[1], 5:[8], 6:[3, 8], 7:[4, 9], 8:[2], 9:[6]}
# 3 5 2 8 6 9 1 4 7
graph = defaultdict(list, graph)
graph_rev = defaultdict(list, graph_rev)
# graph = {1:[4], 2:[8], 3:[6], 4:[7], 5:[2], 6:[9], 7:[1], 8:[5, 6], 9:[3, 7]}
# graph_rev = {1:[7], 2:[5], 3:[9], 4:[1], 5:[8], 6:[3, 8], 7:[4, 9], 8:[2], 9:[6]}

visited = dict()
stack = []
size = 0
# recursionstack = []

def dfs(g, node, _pass):
	global visited, stack, size
	# print(node, end=' ')
	size += 1
	for n in g[node]:
		if n not in visited:
			visited[n] = True
			dfs(g, n, _pass)
			if _pass:
				stack.append(n)

def main():
	global visited, stack, size

	key = 1000000
	scc_size = PriorityQueue()
	start, end = 875714, 0
	# start, end = 9, 0

	for node in range(start, end, -1):
		if node not in visited:
			visited[node] = True
			dfs(graph, node, True)
			stack.append(node)

	# print(stack)

	visited.clear()
	size = 0
	print('pass 1 over')
	
	for node in stack[::-1]:
		if node not in visited:
			dfs(graph_rev, node, False)
			scc_size.put(key-size)
			size = 0

	for i in range(5):
		print(key - scc_size.get() - 1)


if __name__ == '__main__':
	threading.stack_size(67108864)
	sys.setrecursionlimit(800000)
	thread = threading.Thread(target=main)
	thread.start()
