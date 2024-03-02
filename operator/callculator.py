def add(a, b):
    x = int(a)+int(b)
    return x

def min(a,b):
    x=int(a)-int(b)
    return x

def tim(a,b):
    x=int(a)*int(b)
    return x

def div(a,b):
    x=int(a)/int(b)
    return x

print('1. +')
print('2. -')
print('3. *')
print('4. /')
jawab = input('Pilih operator : ')

match jawab:
    case '1':
        a = input('Masuukan angka pertama : ')
        b = input('Masuukan angka kedua : ')            
        print(a,'+',b,'=', add(a,b))
        
    case '2':
        a = input('Masuukan angka pertama : ')
        b = input('Masuukan angka kedua : ')            
        print(a,'-',b,"=", min(a,b))
        
    case '3':
        a = input('Masuukan angka pertama : ')
        b = input('Masuukan angka kedua : ')            
        print(a, "*",b,"=", tim(a,b))

    case '4':
        a = input('Masuukan angka pertama : ')
        b = input('Masuukan angka kedua : ')            
        print(a,"/",b,"=", div(a,b))
        