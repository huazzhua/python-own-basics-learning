
"""
# 全局导入  通过模块名.成员名
import P02_my_add

print(P02_my_add.num)
print(P02_my_add.add(1, 2))


# 全局导入  导入的时候给模块取了别名  通过别名.成员名
import P02_my_add as myadd
print(myadd.num)
print(myadd.add(1, 2))
"""
"""
# 局部导入 方式1   from 模块 import 成员1 as 别名1,成员2 as 别名2...
# from P02_my_add import add
# print(add(1, 2))
# 只能使用导入的成员，未导入的成员不能用
# print(num)

# 如果导入的成员有重名，后导入的成员会将前面的导入成员覆盖掉
# from P04_my_multi import multi,num
# from P02_my_add import add,num
# print(add(1,2))
# print(multi(2,3))
# print(num)

# 可以通过别名 区分重名的成员
from P02_my_add import add,num  as n1
from P04_my_multi import multi,num as n2
print(add(1,2))
print(multi(2,3))
print(n1)
print(n2)

# 导入模块中所有不以单下划线开头的成员
# import P04_my_multi as mymulti
# print(mymulti._str1)

# from P04_my_multi import _str1
# print(_str1)

from P04_my_multi import *
print(num)
print(multi(2,3))
print(_str1)
"""
"""
# 模块的搜索顺序
import sys
print(sys.path)
sys.path.append("./..")
print(sys.path)
# import time
# time.sleep(3)
# print("end")
"""
"""
# __all__限制被导入成员
# import P02_my_add
# print(P02_my_add.num)
# print(P02_my_add.num1)
# print(P02_my_add._str1)
# print(P02_my_add.add(1,2))

# from P02_my_add import num
# from P02_my_add import num1
# from P02_my_add import _str1
# from P02_my_add import add
# print(num)
# print(num1)
# print(_str1)
# print(add(1,2))


from P02_my_add import *
print(_str1)
print(num)
# print(num1)
"""
# __name__属性
import P02_my_add
# from P02_my_add import add
# from P02_my_add import *