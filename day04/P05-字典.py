
# 创建字典对象
# 创建空字典
# dict1 ={}
# dict2 = dict()
# print(type(dict2),dict2)
# dict1 = {"key":"value","key":"value"}

# 创建字典对象方式二
# dict1 = dict(name="zzj",age="24")
# 方式三
# dict1 = dict([("name","zzj"),("age","24"),("gender","boy")])
# print(dict1)

# 字典推导式
# dict1 = {i:i*2 for i in range(5)}
# print(dict1,type(dict1))

# 访问字典元素
# dict1 = dict([("name","zzj"),("age","24"),("gender","boy")])
# print(dict1)
# print(dict1["name"])
# print(dict1["age"])
# print(dict1["gender"])
# 若字典中不存在的key值则报错
# print(dict1["address"])
# print(dict1.get("name"))
# print(dict1.get("age"))
# print(dict1.get("gender"))
# 若字典中不存在的key值则返回none
# print(dict1.get("address"))

# 添加元素

# print(dict1)
# dict1["address"] = "beijing"
# print(dict1)

# 修改元素
# dict1["age"] = 25
# print(dict1)

# 判断元素是否是字典中的值-只针对key,不能针对value
# print("name" is dict1)

# 获取字典长度
# print(len(dict1))

# 删除字典元素
# del dict1["age"]
# print(dict1)

# 字典中的常用方法
dict1 = {"唐僧":"迟重离","悟空":"六小龄童","八戒":"马德华","沙和尚":"阎怀里"}
print(dict1)
# 遍历所有的key
# keys = dict1.keys()
# print(keys,type(keys))
# for key in keys:
    # print(key)

# 遍历所有的value
# values = dict1.values()
# for i in values:
#     print(i)

# 遍历key:value键值对
# for k in dict1.keys():
#     print(k,dict1[k])

for k,v in dict1.items():
    print(k,v)