# 该案例演示了防止函数修改列表

# 浅拷贝需求：不希望在函数中，将列表的数据进行修改
# def change_list(list1):
#     print(f"在函数中，修改列表前列表内容是{list1},地址是{id(list1)}")
#     list1[1] = 20
#     print(f"在函数中，修改列表后列表内容是{list1},地址是{id(list1)}")
#
# list0 = [1,2,3]
# print(f"在函数调用前，修改列表前列表内容是{list0},地址是{id(list0)}")
# # copy()产生了一个新对象
# list00 = list0.copy()
# change_list(list00)
# print(f"在函数调用后，修改列表前列表内容是{list0},地址是{id(list0)}")


# 浅拷贝

# def change_list(list1):
#     print(f"在函数中，修改列表前列表内容是{list1},地址是{id(list1)}")
#     list1[3].append(40)
#     print(f"在函数中，修改列表后列表内容是{list1},地址是{id(list1)}")
#
# list0 = [1,2,3,[10,20,30]]
# print(f"在函数调用前，修改列表前列表内容是{list0},地址是{id(list0)}")
# # copy()产生了一个新对象
# list00 = list0.copy()
# change_list(list00)
# print(f"在函数调用后，修改列表前列表内容是{list0},地址是{id(list0)}")

# 深拷贝

import copy
def change_list(list1):
    print(f"在函数中，修改列表前列表内容是{list1},地址是{id(list1)}")
    list1[3].append(40)
    print(f"在函数中，修改列表后列表内容是{list1},地址是{id(list1)}")

list0 = [1,2,3,[10,20,30]]
print(f"在函数调用前，修改列表前列表内容是{list0},地址是{id(list0)}")
list00 = copy.deepcopy(list0)
change_list(list00)
print(f"在函数调用后，修改列表前列表内容是{list0},地址是{id(list0)}")