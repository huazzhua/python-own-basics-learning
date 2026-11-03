"""
    该案例演示了多态
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.age}岁的{self.name}去吃饭")

class Teacher(Person):
    pass

class Student(Person):
    pass


"""
def 放学吃饭(person):
    person.eat()


fxf = Teacher("fxf",18)
放学吃饭(fxf)

xjq = Student("xjq",20)
放学吃饭(xjq)
"""

def new_obj(num):
    if num == 1:
        obj = Teacher("fxf",18)
    else:
        obj = Student("xjq",20)

    return obj

# obj = new_obj(1)
obj = new_obj(2)
print(obj.name, obj.age)
