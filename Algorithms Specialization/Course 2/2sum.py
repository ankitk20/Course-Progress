import sys, threading

def main():
	with open('2sum.txt', 'r') as file:
	  f = file.readlines()

	f = list((map(lambda x: int(x), f)))
	f.sort()

	lower, upper = -10000, 10000
	sum_seen = [False] * (upper - lower + 1)
	left, right = 0, len(f) - 1

	while left < right:
		_sum = f[left] + f[right]
		# print(_sum, end=' ')
		if _sum > upper:
			right -= 1

		elif _sum < lower:
			left += 1

		else:
			if f[left] != f[right]:
				sum_seen[_sum + upper] = True

			scan_left = left + 1
			scan_right = right - 1

			while scan_left < right:
				_sum = f[scan_left] + f[right]
				if _sum > upper:
					break
				elif f[scan_left] != f[right]:
					sum_seen[_sum + upper] = True
				scan_left += 1

				
			while left < scan_right:
				_sum = f[left] + f[scan_right]
				if _sum < lower:
					break
				elif f[left] != f[scan_right]:
					sum_seen[_sum + upper] = True
				scan_right -= 1

			left += 1
			right -= 1

	print('count = ', sum(sum_seen))



if __name__ == '__main__':
	threading.stack_size(67108864)
	thread = threading.Thread(target=main)
	thread.start()
