class Mobil:
    def __init__(self, tipe, warna):
        self.tipe = tipe
        self.warna = warna
        
pajero = Mobil('SUV','Merah')
camry = Mobil('Sedan', 'Hitam')

for item in (pajero, camry):
    print(item.tipe)
    print(item.warna)
 
