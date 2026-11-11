"""
    该案例演示了带参数的装饰器
"""

from math import sqrt


def times(n):
    def get_absolute(f):
        def inner(x):
            x = abs(x)
            for i in range(n):
                x = f(x)
            return x
        return inner
    return get_absolute

# @times(2)
def func(x):
    """开根号"""
    return sqrt(x)

# print(func(-16))

print(times(2)(func)(-16))
