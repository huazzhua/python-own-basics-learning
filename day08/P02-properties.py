"""
    该案例演示了property
"""
"""
class Person:
    @property # 将方法转换为属性
    def eat(self):
        print("eating")
p = Person()
# p.eat()
p.eat
"""

"""
# Java语言的处理方式，属性私有化，提供公开的get-set方法去获取以及设置属性的值
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def set_age(self, age):
        if age <= 18:
            self.__age = age

    def get_age(self):
        if self.__age > 18:
            return 18
        return self.__age

zsh = Person("zsh",60)
print(zsh.name)
print(zsh.get_age())
zsh.set_age(18)
"""


# Python语言的处理
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        if self.__age > 18:
            return 18
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def name(self):
        return self.name


p1 = Person("zsh", 60)
# print(p1.get_age())
# print(p1.age)
# p1.age = 15
# print(p1.age)