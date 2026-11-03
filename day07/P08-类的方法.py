"""
    该案例演示了方法
"""
"""
class Person:

    # 类属性
    home = "earth"

    def __init__(self, name):
        self.name = name

    def m2(self):
        print("m2222")

    def m1(self):
        print(Person.home)
        print(self.name)
        self.m2()# Person.m2(self)

    @classmethod
    def m3(cls):
        print(cls.home)
        print(cls.__doc__)

    @staticmethod
    def m4():
        print("xxxx")

# zs = Person("zs")
# zs.m3()

# Person.m3()
Person.m4()
"""


def m5(self, x, y):
    print(x + y)


class MyC:
    f1 = m5


MyC().f1(1, 2)