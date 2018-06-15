with open('mwis.txt') as file:
	lines = file.readlines()

weights = [int(line) for line in lines]
nodecount = weights.pop(0)
checklist = [1, 2, 3, 4, 17, 117, 517, 997]

arrayfill = dict()
arrayfill[-1], arrayfill[0], arrayfill[1] = 0, 0, weights[0]

for i in range(2, len(weights)):
	arrayfill[i] = max(arrayfill[i-1], arrayfill[i-2] + weights[i-1])

independentset = set()
hop = len(weights)

while hop > 0:
	if arrayfill[hop-2] + weights[hop-1] <= arrayfill[hop-1]:
		hop -= 1
	else:
		independentset.add(hop)
		hop -= 2

for n in checklist:
	print(1 if n in independentset else 0)
