"""
    该案例演示了一个匿名函数
"""
# 需求：定义一个计算器，完成加减乘除运算
# def calculate(num1,num2,op):
#     if op == '+':
#         return num1+num2
#     elif op == '-':
#         return num1-num2
#     elif op == '*':
#         return num1*num2
#     elif op == '/':
#         return num1/num2
#
# print(calculate(3,4,'+'))

# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1+num2
# def mul(num1,num2):
#     return num1+num2
# def div(num1,num2):
#     return num1+num2
#
# def calculate(num1,num2,op):
#     return op(num1,num2)



# def calculate(num1,num2,op):
#     return op(num1,num2)
# # lambda 匿名函数
# print(calculate(10,20,lambda a,b : a+b))


# 匿名函数使用场景

# student_list = [{"name":"zhangsan","age":36},{"name":"lisi","age":14},{"name":"wangwu","age":27}]
#
# print(sorted(student_list,key=lambda std_list:std_list["age"],reverse=True))

# list1 = [i for i in range(5)]
#
# def op(item):
#     return 'zzj->'+str(item)
#
# # print(list(map(op,list1)))
#
# print(list(map(lambda item:'zzj->'+str(item),list1)))

# 聚合方法

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))