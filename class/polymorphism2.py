class Hewan():
    def suara(self):
      print("Suara hewan")

class Kucing(): 
    def suara(self):
       print("Meow")

    def harapan_hidup(self): 
      print("Harapan hidup kucing adalah 10 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh kucing pada umumnya adalah kuning") 
   
class Anjing(): 
    def suara(self):
      print("Woof")

    def harapan_hidup(self): 
      print("Harapan hidup anjing adalah 15 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh anjing pada umumnya adalah hitam") 
   
obj1 = Kucing() 
obj2 = Anjing() 
for type in (obj1, obj2): # creating a loop to iterate through the obj1, obj2
    type.harapan_hidup() 
    type.warna_tubuh() 
