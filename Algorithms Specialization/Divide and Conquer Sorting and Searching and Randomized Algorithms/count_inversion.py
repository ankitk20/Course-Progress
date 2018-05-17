
def conquer(numbers, temp, left, mid, right):
  i, j, inversion = left, mid, 0
  while i < mid and j <= right:
    temp.append(min(numbers[i], numbers[j]))
    if numbers[i] <= numbers[j]:
      i += 1 
    else:
      j += 1
      inversion += mid - i
    
  if i < mid:
    temp += numbers[i:mid]
  if j <= right:
    temp += numbers[j:right+1]
    
  numbers[left:right+1] = temp
  # print(temp)
  # print('updated', numbers)
  
  return inversion

def divide(numbers, temp, left, right):
  inversion = 0
  if left < right:
    mid = (left + right) // 2;
    inversion += divide(numbers, [], left, mid)
    inversion += divide(numbers, [], mid+1, right)
    # print(temp, left, mid+1, right)
    inversion += conquer(numbers, temp, left, mid+1, right)
  return inversion

def main():
  numbers = []
  with open('input', 'r') as file:
    num = file.readlines()
    numbers = [int(string) for string in num]
  # numbers = [2, 4, 1, 3, 5]
  print(divide(numbers, [], 0, len(numbers)-1))

main()
