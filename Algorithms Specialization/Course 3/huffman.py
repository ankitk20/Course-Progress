from queue import PriorityQueue

with open('huffman.txt') as file:
	lines = file.readlines()

charcount = int(lines.pop(0))
heap = PriorityQueue()
for i in range(len(lines)):
	heap.put((int(lines[i]), i + 1, 0, 0))	# (freq, char, maxlen, minlen)

internalnode = charcount

while heap.qsize() > 1:
	min1 = heap.get()
	min2 = heap.get()
	heap.put((min1[0] + min2[0], internalnode, max(min1[2], min2[2]) + 1, min(min1[3], min2[3]) + 1))
	internalnode += 1

print('(max, min) = ', heap.get()[2:])
