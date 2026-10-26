# 容器数据类型-列表
#
# list1 = [100,200,200,300,100,400,500,300,200]

# 使用下标取数据，从左开始递增从0开始，从右开始递减从-1开始

# 列表取数
# print(list1[1])
# print(list1[-4])

# 列表切片 [起始位置:结束位置:步长] 包含起始不包含结束元素
# print(list1)
# # 复制整个列表
# print(list1[:])
# 取索引2-4的元素
# print(list1[2:4])
# # 取索引2-末尾的元素
# print(list1[2:])
# # 取索引2- -1的元素
#
# print(list1[2:-1])

# 倒叙取所有元素
# print(list1[::-1])


# 列表添加元素
# append-追加-末尾位置
# list1.append(600)
# print(list1)
#
# print(list1.append(600)) # list1.append(600)完成追加没有返回值

# insert-添加-随意指定位置
# list1.insert(0,600)
# print(list1)

# 列表相加
# list2 = [900,800,700,600,500]
# list3 = ["a","b","c"]
# print(list2+list3)
# # 列表相乘
# print(list2 * 2)
# # 列表修改元素
# list2[2] = 123
# print(list2)
#
# # 通过切片修改多个值
# list2[1:3] = [123,456,789]
# print(list2)
#
# # 判断元素是否在列表中
# print(200 in list2)
#
# # 获取列表长度
# print(len(list3))
#
# # 获取列表中最大值，最小值，累加值
#
# print(max(list2))
# print(min(list2))
# print(sum(list2))


# 列表遍历
# ①直接遍历
# for i in list1:
#     print(i)
# ②通过下标遍历
# for i in range(5):
#     print(list1[i])
# ③使用enumerate()同时获取下标与元素
# for i,item in enumerate(list1):
#     print(i,item)


# 列表删除
# remove 删除列表中第一次出现的元素
# list1.remove(200)
# print(list1)
# del 删除指定元素
# del list1[1]
# print(list1)

# 删除列表元素
# print(list1)
# for i in reversed(list1):
#     print(i)
#     if i==200:
#         list1.remove(200)
# print(list1)

# 列表嵌套
# listx = ["a","c","asd","zzk",list1]
# print(listx)


# 列表推导式
# lista = [x*2 for x in range(5)]
# print(lista)

# 带条件的列表推导式
# lista = [item for item in list1 if item != 200]
# print(lista)

# 包含多个循环的列表推导式
# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]
#
# list3 = [(i,j) for i in list1 for j in list2]
#
# print(list3)

# zip函数
# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]
#
# zipped = zip(list1,list2)
# for i in zipped:
#     print(i)

# 列表常用方法
list1 = [1,2,3]
list2 = [4,5,6]
# ①extend 在列表一的末尾添加列表二的数据  注意 使用加法是创建新的对象，原列表数据没变，extend没有创建新对象，就在原列表追加，原列表数据改变
# list1.extend(list2)
# print(list1)

# ②pop 默认删除末尾数据
# list1.pop()
# print(list1)

# ③clear 清空列表
# list1.clear()
# print(list1)