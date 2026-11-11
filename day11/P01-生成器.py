"""
    该案例演示了生成器对象的创建
"""

"""
# 方式1：通过推导式创建生成器
from types import GeneratorType
from typing import Iterator

gen = (i for i in range(100))
print(gen)
# print(next(gen))
# print(next(gen))
from collections.abc import Iterable
print(isinstance(gen, Iterable))   # 判断是否可以迭代
print(isinstance(gen, Iterator))   # 判断是否是迭代器对象

# for i in gen:
#     print(i)
"""
"""
# 方式2：通过类似标准函数形式创建生成器
def fibo():
    a , b = 0 , 1
    while True:
        # 生成器通过yield进行值的返回
        yield b
        a, b = b, a+b

f = fibo()
# print(type(f))
print(next(f))
print(next(f))
print(next(f))


print(next(f))
print(next(f))
print(next(f))
print(next(f))
"""

# 获取生成器函数的返回值
def fibo():
    a , b ,count = 0 , 1,0
    while count < 10:
        # 生成器通过yield进行值的返回
        yield b
        a, b ,count = b, a+b ,count+1
    return "65432321done123456"

f = fibo()
try:
    while True:
        print(next(f))
except StopIteration as e:
    print(e)