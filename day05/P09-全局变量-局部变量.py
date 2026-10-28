"""
    该案例演示了全局变量以及局部变量和global、nonlocal关键字
"""
# 全局变量以及局部变量
# 全局变量：定义在模块下，函数外，可以被当前模块的所有内容访问
# 局部变量：定义在函数内，只能被当前函数访问

# 全局变量
# var0 = 10
# # 局部变量之间相互独立
# def func_1():
#     var1 = 20
#     # 在函数体中，可以访问全局变量
#     print(var0)
#     # 在函数体中，可以访问自己定义的局部变量
#     print(var1)
#
# def func_2():
#     var2 = 30
#     # 在函数体中，可以访问全局变量
#     print(var0)
#     # 在函数体中，可以访问自己定义的局部变量
#     print(var2)

# 局部有限

# var1 = 10
#
# def func():
#     # 如果在函数体中，对变量进行赋值操作，python会将变量当成局部变量进行处理
#     # 哪怕存在着同名的局部变量
#     # var1 = 100
#     var1 += 100
#     print(var1)
#
# func()
# 如果在函数体中，对全局变量做修改
# var1 = 10
# def func():
#     # 声明当前在函数体中的变量为全局变量，这个时候，不会在单独创建局部变量
#     global var1
#     var1 = 100
#     print(var1)
# func()
# print(var1)



# var1 = [1,2,3]
# def func():
#     # 严格说 var1[1] = 20 属于修改操作，操作的还是全局变量
#     # var1[1] = 20
#     # 以下操作属于赋值操作
#     var1 = [2,3,4]
#     print(var1)
# func()
# print(var1)


def outer():
    var1 = 10
    def inner():
        # nonlocal 标记使用嵌套变量
        nonlocal var1
        var1 = 20
        print(var1)
    inner()
    print(var1)
outer()


