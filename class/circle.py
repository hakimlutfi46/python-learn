class Circle:
  PI = 3.1415
  def __init__(self,name,radius):
    self.__name = name # instance variable
    self.__radius = radius # instance variable
  
  # menghitung area sebuah lingkaran dengan pi * r kuadrat
  # method dari class Circle dan instance akan mengambil value PI dari class variable melalui Circle.PI
  def area(self):
    return Circle.PI * self.__radius ** 2

c1 = Circle("C1",4)
print("Area dari c1:",c1.area())

c2 = Circle("C2",6,)
print("Area dari c2:",c2.area())

c3 = Circle("C3",5)
print("Area dari c3:",c3.area())

