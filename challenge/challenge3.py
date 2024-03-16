# cara 1
# fungsi sum untuk menjumlahkan element pada subarray

# num = [[1,2,3], [2,3,4], [3,4,5]]

# total = [sum(subarray) for subarray in num]

# print(total)

#cara 2

num = [[1,2,3], [2,3,4], [3,4,5]]
sums = []

for subarray in num:
    total = 0
    for num in subarray:
        total += num
    sums.append(total)

print(sums)


