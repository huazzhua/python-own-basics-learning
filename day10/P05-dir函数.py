"""
    该案例演示了dir函数
"""
"""
# 你将一个模块作为 dir() 的参数时，它会返回该模块中定义的名称列表，包括函数、类、变量等
# import math
# print(dir(math))
"""
"""
#当你将一个对象作为 dir() 的参数时，它会返回该对象的属性和方法列表
class MyClass:
    def __init__(self):
        self.x = 1
        self.y = 2

    def method1(self):
        pass
obj = MyClass()
print(dir(obj))
"""
"""
# 传递类对象给dir函数
class MyClass:
    name = "atguigu"
    def __init__(self):
        self.x = 1
        self.y = 2

    def method1(self):
        pass
print(dir(MyClass))
"""

def my_function():
    pass
variable = 10

print(dir())
