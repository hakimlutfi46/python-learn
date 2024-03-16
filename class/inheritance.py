class Person: # Parent class
  nama = 'test'

class Employee(Person): # Child class (subclass)
  gaji = 1000
  
person1 = Person()
employee1 = Employee()

print('nama dari person:', person1.nama)
print('nama dari employee:', employee1.nama) # Employee mewarisi atribut nama dari Person
print('gaji dari employee:', employee1.gaji)
