# 创建集合对象
# set1 = {1,2,3}
# 将列表转换为集合，一般用于去重场景
# set2 = set([1,2,2,3,3])
# print(set1,set2)

# 定义一个空集合
# set1 = {}
# set2 = set()
# print(type(set1),type(set2))

# 通过集合推导式创建集合对象
# set1 = {i*2 for i in range(5)}
# print(set1)


# 往集合中添加元素
# set1 = {1,2,3}
# set1.add(4)
# print(set1)
# 从集合中删除元素
# set1.remove(3)
# print(set1)
# 检查成员是否为集合中的元素
# print(2 in set1)


# set常用方法

set1 = {1,21,3,4,5,61,7,8}
# set1.add(4) # 添加元素只能添加一个元素
# print(set1)
set2 =  {3,4,5,7,9,13,51}
# set1.update([6])
# print(set1)
# set1.update(set2) # 添加元素，元素可以是列表，元组，字符串，字典等可迭代对象-并且会去重
# print(set1)
# set1.union(set2)
# print(set1)  # 添加元素后返回的是一个新的集合，因为创建了一个新对象，元素可以是列表，元组，字符串，字典等可迭代对象-并且会去重

# 移除元素
# set1.remove(3) # 从集合中移除元素x,不存在报错
# print(set1)
# set1.discard(3) # 从集合中移除元素x,不存在不会报错
# print(set1)
# pop()随机从集合中取出一个元素，如果集合为空则报错
# set1.pop()
# print(set1)
# clear()清空集合元素
# set1.clear()
# print(set1)

# set.difference(x) 求set和x的差集，返回一个新集合
# set3 = set1.difference(set2)
# print(set1)
# print(set3)
# set.difference_update 求set和x的差集,直接对原集合进行操作
# set1.difference_update(set2)
# print(set1)

# set.intersection(x) 求set和x的交集，返回一个新集合
# set3 = set1.intersection(set2)
# print(set1)
# print(set3)
# set.intersection_update() 求set和x的交集,直接对原集合进行操作
# set1.intersection_update(set2)
# print(set1)

# set1 & set2 求两个集合的交集，set1 | set2 求两个集合的并集 ，set1 - set2 求两个集合的差集
# print(set1 & set2)
# print(set1 | set2)
# print(set1 - set2)
# print(set1)

# set.isdisjoint(x) 判断两个集合是否没有交集
# print(set1.isdisjoint(set2))
# set.issubset(x) 判断set是否为x的子集
# print(set1.issubset(set2))
# set.issuperset(x) 判断set是否是x的父集
# print(set1.issuperset(set2))


# set.symmetric_difference(x)  求两个集合中不重复的元素，返回一个新集合
# print(set1.symmetric_difference(set2))
# print(set1)
# set.symmetric_difference_update(x)  求两个集合中不重复的元素，直接对原集合进行操作
# set1.symmetric_difference_update(set2)
# print(set1)

# 拷贝集合
set3 = set1.copy()
print(set3)
print(set1)
print(id(set1),id(set3))