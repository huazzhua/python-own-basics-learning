"""
    该案例演示了类装饰器
"""
from math import sqrt
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        x = abs(x)
        return self.func(x)


# @DecoratorClass
def func(x):
    """开根号"""
    return sqrt(x)


# print(func(-4))

# 创建类的实例
d = DecoratorClass(func)
print(d(-4))
