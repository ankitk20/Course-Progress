from collections import defaultdict

with open('2sat2.txt', 'r') as file:
    f = file.readlines()

f.pop(0)
propdict = defaultdict(list)
proplist = list()

for line in f:
	a, b = tuple(map(int, line.split()))
	propdict[a].append(b)
	proplist.append((a, b))

# print(propdict)
keylist = list(propdict.keys())
index = 0
satisfy = True
while True:
	print(index, len(keylist))
	# print(keylist)
	if index == len(keylist):
		break
	key = keylist[index]
	if -key in propdict:
		found = False
		# print(len(propdict[key]), len(propdict[-key]))
		for i in range(len(propdict[key])):
			for j in range(len(propdict[-key])):
				if propdict[key][i] == -propdict[-key][j]:
					found = True
					propdict[key].pop(i)
					propdict[-key].pop(j)
					break
			if found:
				break

		if not found:
			newkey = propdict[key].pop()
			newval = propdict[-key].pop()
			propdict[newkey].append(newval)

		if len(propdict[key]) == 0:
			del propdict[key]
		if len(propdict[-key]) == 0:
			del propdict[-key]
		i = 0
		# print('i reset', i)
	else:
		found = spfound = False
		for i in range(len(propdict[key])):
			if -propdict[key][i] in propdict:
				found = True
				otherkey = -propdict[key][i]
				for j in range(len(propdict[otherkey])):
					if key == -propdict[otherkey][j]:
						spfound = True
						propdict[otherkey].pop(j)
						propdict[key].pop(i)
						if len(propdict[key]) == 0:
							del propdict[key]
						if len(propdict[otherkey]) == 0:
							del propdict[otherkey]
						break

				if not spfound:			
					propdict[key].pop(i)
					transfer = propdict[otherkey].pop()
					propdict[key].append(transfer)
					if len(propdict[otherkey]) == 0:
						del propdict[otherkey]
				break

		if not found:
			# print(index, 'not found')
			index += 1
			continue
		else:
			i = 0
			# print('i reset', i)

	# print(propdict)
		
	keylist = list(propdict.keys())

print(propdict)
print(1 if len(propdict) else 0)