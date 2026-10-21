# # input 打印函数
#
# name = input("请输入你的名字")
# age = input("请输入你的年龄")
# print(name+"的年龄是"+age)

# # print 可以打印输出多个值，中间用，分割
# print("曾志坚","学python","第二天")
#
# # 可以使用end= 来控制print()以什么结尾
#
# print("hello",end="")
# print("world")
#
# print("hello",end="\n")
# print("world")

# 格式化输出
# 1.字符串使用%占位 %d-十进制整数，%f-浮点数，%s-字符串，%o-八进制数，%x-十六进制数，%e-科学计数法
# int1 = 10
# float1 = 3.14
# str1 = "int1=%d，float=%f" % (float1,int1)
# print(str1)
# 2.字符串，format
# 方法①-不设置指定位置，按默认顺序
# int1 = 10
# float1 = 3.1415
# bool1 = True
# str1 = "int1={},float={},bool1={}".format(int1,float1,bool1)
# print(str1)
# # 方法②-设置指定变量，不能和方法①混合使用
# int1 = 10
# float1 = 3.1415
# bool1 = True
# str1 = "int1={2},float={0},bool1={1}".format(int1,float1,bool1)
# print(str1)
#
# # 方法③-设置参数
# int1 = 10
# float1 = 3.1415
# bool1 = True
# str1 = "int1={a},float={b},bool1={c}".format(a=int1,b=float1,c=bool1)
# print(str1)


# 数字格式化
# *-指定填充字符，^指定对齐方式-居中，<-左对齐，>-右对齐
# 指定输出20个字符，如果不够，用指定字符进行填充，默认是空格
# .或者_ 每3位进行分隔
# float1 = 3.14159
# str2 = "{:*^20,.2f}".format(float1)
# print(str2)

# f"字符串"
int1 = 10
float1 = 3.1415
bool1 = True
str1 = f"int1={int1},float={float1},bool1={bool1}"
print(str1)
