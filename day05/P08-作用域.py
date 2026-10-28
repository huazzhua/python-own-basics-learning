"""
    该案例演示了作用域
"""
a = int(10.0)   # 全局作用域   int:内建作用域

def outer():
    # a = 20 # 嵌套作用域
    def inner():
        # a = 30  # 局部作用域
        print(a)
    return inner
outer()()