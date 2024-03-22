def mergesort1(S):
  n = len(S)
  if n > 1:
    print(S)
    mid = n // 2
    L, R = S[:mid], S[mid:]
    mergesort1(L)
    mergesort1(R)
    merge1(S,L,R)

def merge1(S,L,R):
  k = 0
  while len(L) > 0 and len(R) > 0:
    if L[0] <= R[0]:
      S[k] = L.pop(0)
    else:
      S[k] = R.pop(0)
    k += 1
  
  while len(L) != 0:
    S[k] = L.pop(0)
    k += 1
  while len(R) != 0:
    S[k] = R.pop(0)
    k += 1
    
    
    
S = [27,10,12,20,25,13,15,22]
mergesort1(S)
print(S)