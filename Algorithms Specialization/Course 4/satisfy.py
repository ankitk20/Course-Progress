from collections import defaultdict

with open('2sat2.txt', 'r') as file:
    f = file.readlines()

f.pop(0)
propdict = defaultdict(lambda: defaultdict(bool))
proplist = list()

for line in f:
	a, b = tuple(map(int, line.split()))
	propdict[a][b] = True
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
		for i in propdict[key]:
			# for j in range(len(propdict[-key])):
			if -i in propdict[-key]:
				found = True
				del propdict[key][i]
				del propdict[-key][-i]
				break

		if not found:
			newkey = next(iter(propdict[key]))
			newval = next(iter(propdict[-key]))
			propdict[newkey][newval] = True
			del propdict[key][newkey]
			del propdict[-key][newval]

		if len(propdict[key].keys()) == 0:
			del propdict[key]
		if len(propdict[-key].keys()) == 0:
			del propdict[-key]
		i = 0
		# print('i reset', i)
	else:
		found = spfound = False
		for i in propdict[key]:
			if -i in propdict:
				found = True
				otherkey = -i
				if -key in propdict[otherkey]:
					spfound = True
					del propdict[otherkey][-key]
					del propdict[key][i]
					if len(propdict[key]) == 0:
						del propdict[key]
					if len(propdict[otherkey]) == 0:
						del propdict[otherkey]

				else:
					del propdict[key][i]
					transfer = next(iter(propdict[otherkey]))
					propdict[key][transfer] = True
					del propdict[otherkey][transfer]
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

print(1 if len(propdict) else 0)