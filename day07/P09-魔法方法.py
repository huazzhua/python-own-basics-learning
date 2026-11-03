"""
    该案例演示了魔法方法
"""

class Person:
    # def __del__(self):
    #     print("del被执行了")
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + str(self.age)

    def __getattribute__(self, item):
        print(item +"~~~~~")
        return object.__getattribute__(self, item)


p = Person("zs",20)
print(p.age)
# print(p)