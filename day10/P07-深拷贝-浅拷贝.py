"""
    该案例演示了深拷贝与浅拷贝
"""
# 浅拷贝
# 方式一
list1 = [1,2,3]
# list2 = list1[:]
# print(id(list1),id(list2))

# 方式二
# list2 = list(list1)
# print(id(list1),id(list2))

# 方式三
# list2 = list1.copy()
# print(id(list1),id(list2))

# 方式四

# 深拷贝
# import copy
# list2 = copy.deepcopy(list1)
# print(id(list1),id(list2))


import copy

list1 = [1, 2, 3, [100, 200, 300]]
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# 还有浅拷贝使用查看结果-copy.copy(list1)
list2 = copy.deepcopy(list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)


print("~~~~~~~")
# list1[0] = 100
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)


list1[3].append(400)  # 修改list1[3]列表元素，向列表中添加新值
print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)
"""
"""
# 非容器类型（如数字、字符串、和其他“原子”类型的对象）无法拷贝
import copy

var1 = 1
print(id(var1), var1)

var2 = copy.copy(var1)
print(id(var2), var2)

var3 = copy.deepcopy(var1)
print(id(var3), var3)
"""
# 元组变量如果只包含原子类型对象，则不能对其深拷贝
import copy

# tuple1 = (1, 2, 3)  # 元组只包含原子类型对象
tuple1 = (1, 2, 3,[])  # 元组中包含了可变类型对象
print(id(tuple1), tuple1)

tuple2 = copy.deepcopy(tuple1)
print(id(tuple2), tuple2)
"""

