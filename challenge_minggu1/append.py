x = [1,2,3,4,5,6,7,8,9,10]

genap = []
ganjil = []

for item in x:
    if item%2==0:
      genap.append(item)
    else:
        ganjil.append(item)
        
print('list awal ',x)        
print('ini list genap ',genap)
print('ini list ganjil ',ganjil)
 

