# 该案例演示了函数说明文件

# def adult(age):
#     """ 该函数用于判断是否成年"""
#     return "成年" if age > 10 else "未成年"
# print(adult(24))
# help(adult)

# 该案例演示函数的返回值
# 如果没加return,在函数体的最后一行会自动隐式添加return，表示函数执行结束，没有返回值，调用者接受到none
# def func():
#     print(123)

# print(func())

# 如果有return关键字，但是return后面没有任何跟任何内容，同样返回none

# def func():
#     print(123)
#     return
# print(func())

# 有返回值的情况
# def sum(num1,nunm2):
#     sum = num1+nunm2
#     return sum
#
# print(sum(4,15))


# 在python中，return可以返回多个值，多个值会放到元组中
# def func(a,b,c):
#     return a,b,c,(a,b,c)
#
# res = func(1,2,3)
# print(res)

def func():
    for i in range(10):
        if i == 5:
            # continue
            # break
            return
        print(i)
    print("循环结束了！")

func()