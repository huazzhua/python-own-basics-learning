"""
 二进制--0b开头
 八进制--0o
 十六进制--0x

  数据类型
  可变类型--列表，集合，字典
  不可变类型--数值，字符串，元组
"""


# f1 = 0.123
# f2 = 0.456
# f3 = f1+f2
# print(type(f3))
#
# # 精度丢失，在任何编程语言中浮点数类型都存在精度丢失问题
#
# print(f3)

# 解决精度丢失使用 decimal
# from decimal import Decimal
#
# f1 = Decimal("0.1")
# f2 = Decimal("0.2")
# f3 = f1+f2
# print(f3)