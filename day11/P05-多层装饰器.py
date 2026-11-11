"""
    该案例演示了多层装饰器
"""
"""
# 多层装饰器  语法糖形式
from math import sqrt

def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

@get_integer
@get_abs
def func(x):
    return sqrt(x)

print(func("-4"))
"""

# 多层装饰器  手动调用形式
from math import sqrt

def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

def get_integer(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

def func(x):
    return sqrt(x)

abs_inner = get_abs(func)
int_inner = get_integer(abs_inner)
print(int_inner("-4"))

# 以下调用顺序是错的
# int_inner = get_integer(func)
# abs_inner = get_abs(int_inner)

