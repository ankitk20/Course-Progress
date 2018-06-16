with open('knapsack1.txt') as file:
	lines = file.readlines()

val_weight = list(map(lambda x: tuple(map(int, x.split())), lines))
W = val_weight.pop(0)[0]

def knapsack(W, n):
	global val_weight
	table = [[0 for x in range(W+1)] for x in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if 0 in (i, w):
				table[i][w] = 0
			elif val_weight[i-1][1] <= w:
				table[i][w] = max(val_weight[i-1][0] + table[i-1][w-val_weight[i-1][1]],  table[i-1][w])
			else:
				table[i][w] = table[i-1][w]

	return table[n][W]
 
ans = knapsack(W, len(val_weight))
print(ans)