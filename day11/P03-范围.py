"""
    该案例回顾了命名空间、作用范围、以及闭包
"""
"""
# 闭包
def outer(a,b):
    def inner(x):
        return a * x + b
    return inner


# print(outer(2, 3)(5))
inn = outer(10,23)
cells = inn.__closure__
# print(cells)
print(cells[0].cell_contents)
print(cells[1].cell_contents)
"""
# Local->Enclosing->Global->Built-in
a = int(10.0)

def outer():
    # a = 20
    def inner():
        # a = 30
        print(a)
    return inner

outer()()