"""
    该案例演示了实例属性
"""
class Person:
    """人的类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def eat(self):
    #     self.gender = "男"
    #     print("eating")


zs = Person("zs",20)
print(zs.name)
# print(zs.gender)
zs.gender = "男"
zs.name = "zss"
print(zs.name)
print(zs.gender)

# ls = Person("ls",30)
# print(ls.name)
# print(ls.age)
# print(ls.gender)