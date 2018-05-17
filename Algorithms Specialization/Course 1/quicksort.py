
with open('input', 'r') as file:
  f = file .readlines()
  number = [int(string) for string in f]
# number = [3, 8, 2, 5, 1, 14, 7, 6, 10]
# number = [55, 8, 14, 7, 6, 100, 1, 25, 11, 11]
comparisons = 0

def median(start, end):
  middle = (start + end) // 2
  s, m, e = number[start], number[middle], number[end]
  if s < m < e or e < m < s:
    return middle
  elif m < s < e or e < s < m:
    return start
  else:
    return end

def quicksort(start, end):
  
  global comparisons
  
  if start >= end:
    return

  comparisons += end - start
  
  med = median(start, end)
  # number[start], number[end] = number[end], number[start]    # last element as pivot
  number[start], number[med] = number[med], number[start]    # median element as pivot
  pivot, pivot_point = number[start], start
  i = j = start + 1
  
  while i <= end and j <= end:
    
    if number[j] < pivot and number[i] >= pivot:
      number[i], number[j] = number[j], number[i]
      pivot_point = i
      i += 1
    
    elif number[i] < pivot:
      pivot_point = i
      i += 1
    

    j += 1
    
  number[start], number[pivot_point] = number[pivot_point], number[start]
    
  quicksort(start, pivot_point - 1)
  quicksort(pivot_point + 1, end)
  # print(i, number)
  
    

def main():
  global comparisons
  quicksort(0, len(number)-1)
  print(comparisons)

main()


# 162085
# 164123
# 138382
