from collections import defaultdict

with open('2sat1.txt', 'r') as file:
    f = file.readlines()

propcount = int(f.pop(0))
propdict = defaultdict(set)
proplist = list()

satisfy = True
for line in f:
	a, b = tuple(map(int, line.split()))
	propdict[a].add(b)
	proplist.append((a, b))

# print(propdict)
keylist = list(propdict.keys())

while True:
	key = keylist[0]
	satisfy = True
	satisficationcheck = len(keylist)
	if -key in propdict:
		satisfy = False
		for elem in propdict[key]:
			if -elem in propdict[-key]:
				propdict[key].remove(elem)
				propdict[-key].remove(-elem)
			break
		newset = propdict[key] | propdict[-key]
		if len(newset) == 0:
			del propdict[key]
			del propdict[-key]
		elif len(propdict[key]) == 0:
			del propdict[key]
			propdict[-key] = newset
		elif len(propdict[-key]) == 0:
			del propdict[-key]
			propdict[key] = newset
		else:
			newkey = newset.pop()
			propdict[newkey] = newset
	else:
		newset = propdict[key]
		for elem in propdict[key]:
			if -elem in propdict:
				satisfy = False
				propdict[key].remove(elem)
				newset = propdict[key] | propdict[-elem]
				del propdict[-elem]
				break

		propdict[key] = newset
		if len(propdict[key]) == 0:
			del propdict[key]

	if len(propdict) == satisficationcheck:
		satisfy = True
		break


	# print(propdict)

	if len(propdict) == 0 or satisfy:
		break
		
	keylist = list(propdict.keys())

print(1 if satisfy else 0)