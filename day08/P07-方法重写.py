"""
    该案例演示了方法的重写
"""
"""
class Person:
    def eat(self):
        print("person eat")


class Student(Person):

    def eat(self):
        print("student eat")


s = Student()
s.eat()
"""
"""
# class Person:
#     def eat(self,a,b):
#         print("person eat")



class Student:
    def eat(self, a, b):
        print("person eat")

    def eat(self,a):
        print("student eat")

print(Student.__mro__)
s = Student()
s.eat(10,20)
"""

class Person:
    def eat(self,a):
        print("person eat")

class Student(Person):
    def eat1(self, a, b):
        # Person.eat(self,a)
        # super().eat(a)
        self.eat(a)
        print("Student eat")


print(Student.__mro__)
s = Student()
s.eat1(10,20)

