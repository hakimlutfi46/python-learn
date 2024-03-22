def seq_search(nums,x):
  for i in range(len(nums)): # mencari di seluruh elemen nums
    if x == nums[i]:
      return i # mengembalikan index elemen yang cocok dengan x
  
  return -1 # ketika tidak ditemukan elemen yang cocok dengan x dalam nums

S = [11,37,45,26,59,28,17,53]
x = 53
pos = seq_search(S,x) # fungsi untuk sequential search
print(f"Posisi bilangan {x} didalam list S adalah posisi nomor {pos}")
