#program for access specifiers in python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__mob = "1234567890"
p1 = Person("sandhya", 21)
print(p1.name)
print(p1._age)
# print(p1.__mob) 