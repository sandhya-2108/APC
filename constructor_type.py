#default constructor
class Student:
    def __init__(self):
        self.name = "sandhya"
        self.age = 21
        self.grade = "A+"
        
s = Student()
print("Name:", s.name)
print("Age:", s.age)
print("Grade:", s.grade)

#parameterized constructor
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
r = Rectangle(10, 5)
print("Length:", r.length)
print("Breadth:", r.breadth)