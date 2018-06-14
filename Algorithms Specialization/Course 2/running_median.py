from heapq import heapify, heappush, heappop
from collections import defaultdict

with open('Median.txt', 'r') as file:
  f = file.readlines()

# f = ['10', '15', '25', '24', '36', '11', '44', '17', '29', '14']
f = list(map(lambda x: int(x), f))
ans = 0
mod = 10000

heaphigh = list()	# min heap
heaplow = list()	# max heap
lenh, lenl = 0, 0

heaphigh.append(f[0])
heaplow.append(-f[1])

heapify(heaphigh)
heapify(heaplow)

ans = f[0]%mod + f[1]%mod
f.pop(0)
f.pop(0)

for num in f:
	# print(num)
	if (num >= heaphigh[0] or -heaplow[0] <= num < heaphigh[0]) and lenh <= lenl:
		heappush(heaphigh, num)
		lenh += 1
	elif (num <= -heaplow[0] or -heaplow[0] < num <= heaphigh[0])and lenl <= lenh:
			heappush(heaplow, -num)
			lenl += 1
	else:
		if lenh > lenl:
			transfer = heappop(heaphigh)
			heappush(heaphigh, num)
			heappush(heaplow, -transfer)
			lenl += 1
		else:
			transfer = -heappop(heaplow)
			heappush(heaplow, -num)
			heappush(heaphigh, transfer)
			lenh += 1
	if lenl >= lenh:
		median = -heaplow[0]
	elif lenh > lenl:
		median = heaphigh[0]

	# print(median, heaplow, heaphigh)
	ans += median%mod

ans %= mod
print(ans)
