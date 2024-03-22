def partition1(S,low,high):
  pivot = S[low]
  left, right = low + 1, high
  while left < right:
    print(S)
    while left <= right and S[left] <= pivot:
      left += 1
    while left <= right and S[right] >= pivot:
      right -= 1
    if left < right:
      S[left],S[right] = S[right],S[left]
  pivotpoint = right
  S[low], S[pivotpoint] = S[pivotpoint], S[low]
  return pivotpoint

def quicksort1(S,low,high):
  if low < high:
    print(S)
    pivotpoint = partition1(S,low,high)
    quicksort1(S,low,pivotpoint - 1)
    quicksort1(S, pivotpoint + 1,high)
    

S = [25,22,20,15,13,12,10]
quicksort1(S,0,len(S) - 1)
print(S)
    