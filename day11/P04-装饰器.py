"""
    该案例演示了装饰器
"""
from math import sqrt




"""
# 闭包实现装饰器
def decorator(f):
    count = 0
    def inner(x):
        nonlocal count
        print(count,"~~~~")
        count = count +  1
        x = abs(x)
        return f(x)
    return inner
inn = decorator(func)
print(inn(-4))

def decorator(f,x):
    count = 0
    print(count, "~~~~")
    count = count + 1
    x = abs(x)
    return f(x)

print(decorator(func,-4))
"""

# 装饰器语法糖
def decorator(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

@decorator
def func(x):
    """求开根号"""
    return sqrt(x)

print(func(-4))