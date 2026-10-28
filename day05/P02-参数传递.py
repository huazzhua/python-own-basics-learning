

# 参数不可变传递
#
# def change_int(a):
#     print(f"在函数体内，修改前a的值是{a},地址是{id(a)}")
#     a=10
#     print(f"在函数体内，修改后a的值是{a},地址是{id(a)}")
#
# b = 2
# print(f"在函数体外，调用函数后，b的值是{b},地址是{id(b)}")
# change_int(b)
# print(f"在函数体外，调用函数后，b的值是{b},地址是{id(b)}")



# 参数可变传递
#
# def change_int(list1):
#     print(f"在函数体内，修改前a的值是{list1},地址是{id(list1)}")
#     list1[2]=10
#     print(f"在函数体内，修改后a的值是{list1},地址是{id(list1)}")
#
# list0 = [2,3,4]
# print(f"在函数体外，调用函数前，list0的值是{list0},地址是{id(list0)}")
# change_int(list0)
# print(f"在函数体外，调用函数后，list0的值是{list0},地址是{id(list0)}")



# def change_int(list1):
#     print(f"在函数体内，修改前a的值是{list1},地址是{id(list1)}")
#     list1= list1 *2
#     print(f"在函数体内，修改后a的值是{list1},地址是{id(list1)}")
#
# list0 = [2,3,4]
# print(f"在函数体外，调用函数前，list0的值是{list0},地址是{id(list0)}")
# change_int(list0)
# print(f"在函数体外，调用函数后，list0的值是{list0},地址是{id(list0)}")

# 必须参数(按照参数的位置进行匹配)
# def print_info(a,b,c):
#     print(a,b,c)
#
# print_info(1,2,3)

# 关键字参数(按照参数的名称进行匹配)
# def print_info(name,age):
#     print(name,age)
#
# # print_info("zzj",20)
# print_info(name="zzj",age=20)
# # 关键字参数允许调用的时候与参数声明的顺序不一致
# print_info(age=20,name="zzj")

# 默认值参数
# def print_info(name="zzj",age=13):
#     print(name,age)
#
# # print_info("zzj",20)
# print_info()
# # 关键字参数允许调用的时候与参数声明的顺序不一致
# print_info()

# 不定长参数(可变长参数) 形式1: *参数名
# 若不定长参数后面还有参数，必须使用关键字参数
# def print_info(name,*args,age):
#     print(name,args,age)
#
# print_info('zzj',1,2,3,4,5, age=20)
# 使用两个星号 ** 的参数会以字典的形式导入，后面就不能再有其他参数了
def print_info(name,**args):
    print(name,args)

print_info('zzj',a=1,b=2,c=3,d=4,e=5)










