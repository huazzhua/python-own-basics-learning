"""
    该案例演示了闭包操作
"""

# 需求:在一个函数的函数体中，访问另一个函数中定义的变量

# def outer():
#     a = 10
#     inner(a)
#
# def inner(a):
#     print(a)


def outer():
    a = 10
    def inner():
        print(a)
    return inner
# outer()()
f = outer()
f()

