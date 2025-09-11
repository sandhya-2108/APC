class Person:
  def __init__(self, name, department):
    self.name = name
    self.department = department

p1 = Person("Sandhya", "CSE")

print(p1.name)

#program for destructor in python
class Car:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created")
        
    def __del__(self):
        print(f"{self.name} is destroyed")
car1 = Car("Toyota")
del car1
