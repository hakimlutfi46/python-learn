def selectionsort(S):
  n = len(S)
  for i in range(n - 1):
    print(S) #melihat prosesnya
    smallest = i
    for j in range(i + 1,n):
      if S[j] < S[smallest]:
        smallest = j
    S[i], S[smallest] = S[smallest], S[i]

S = [50,30,40,80,10,70,20,60]
print("Sebelum di sortir", S)
selectionsort(S)
print("Setelah di sortir", S)