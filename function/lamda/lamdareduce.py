from functools import reduce

def sumTwo(a,b):
    return a+b

result = reduce(sumTwo, [1, 2, 3, 4])
print(result)

# dibawah ini dengan menggunakan lambda

a = [1,2,3,4]
n = reduce(lambda x,y : x + y, a)
print(n)

# mekanismenya adalah nanti a akan ditambahkan misal 
# 1+2 = 3. lalu hasilnya akan ditambahkan 3 yag mana hasilnya 6. lalu hasilnya akan ditambahkan lagi dengan 4 
# maka hasilnya 6+4 = 10



c = [1,2,3]
d = reduce(lambda x,y : x + (x*y), c)
print(d)