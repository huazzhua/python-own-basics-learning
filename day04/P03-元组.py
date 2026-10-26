# 创建元组
# tup1 = (1,2,3)
# tup2 = (6)
# 如果元组中只有一个元素，那么元素后面需要加，不然就是整数
# print(type(tup2),type(tup1))

# 可以使用推导方式创建元组对象
# 列表推导式
# list1 = [i*2 for i in range(5)]
# print(list1,type(list1))

# 元组推导式
# 注意：这里创建的是生成器对象
# sup1 = (i*2 for i in range(5))
# print(sup1,type(sup1))
# print(tuple(sup1))

# 访问元组
# tup1 = (100,200,300,400,500)
# print(tup1[2])
# print(tup1[-3])
# print(tup1[2:])

# 元组相加
# tup2 = ('a','b','c')
# print(tup1+tup2)

# 元组相乘
# print(tup1*3)
#
# print(300 in tup1)


# 遍历元组
# for i in tup1:
#     print(i)
# for i in range(len(tup1)):
#     print(tup1[i])

# 元组不可变
tup1 = (100,200,300,400,500)
tup2 = (400,)
print(tup1,id(tup1))
print(tup1+tup2)