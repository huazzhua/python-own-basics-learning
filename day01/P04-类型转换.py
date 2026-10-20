# num1 = 10
# num2 = 15.5
# print(type(num1))
# print(type(num2))
# # 小类型数据+大类型数据，自动升级为大类型数据--隐式类型转换
# num3 = num1+num2
# print(type(num3))
#
# # 特殊情况
# num4  = 6
# num5  = 2
# num6 = num4/num5
# print(num6)
# print(type(num6))

# 整数和字符串相加操作会导致报错,只能使用强制转化解决

# age = 18
# print("班里有个叫小明，年龄"+str(age))
# # int（x,base=xxx）将x转化为一个整数，x若为字符串可用base指定进制
# var = int("1010",base=2)
# print(var,type(var))

# float（x,base=xxx）将x转化为一个浮点数数
# var = float("10.10")
# print(var,type(var))

# complex(real[，imag])，创建一个师部real，虚部为imag的复数
# print(complex(3,5))

# eval执行x字符串表达式，并返回表达式的值
# eval("print(123)")

# ord(x) 将一个字符转换为它的ASCII整数值
print(ord('A'))

# chr(x) 将一个整数转化为一个unicode字符
print(chr(66))