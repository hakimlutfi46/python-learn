def bubblesort(S):
  n = len(S)
  for i in range(n):
    print(S) # untuk mengetahui proses yang terjadi
    for j in range(n - 1):
      if S[j] > S[j + 1]:
        S[j], S[j + 1] = S[j + 1], S[j]
        

S = [50,30,40,10,20]
print(f"Sebelum di short {S}")

bubblesort(S)
print(f"Setelah di short {S}")