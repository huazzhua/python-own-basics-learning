# 创建字符串

# str1 = 'hello'
# str2 = "hello"
# str3 = """hello"""
#
# print(str3)

# 访问字符串

# str1 = 'abcdefg'

# print(str1[3])
# print(str1[-4])
# print(str1[2:5]) # 包含起始不包含结束
# print(str1[2:])
# print(str1[::-1]) # 倒序输出

# str2 = "hello world!"
# print(str1+str2)
# print(str1)
#
# # 字符串相乘
# print("~"*20)
# # 判断字符是否在字符串中
# print("abc" in str1)

# 原始字符串
# print("hello \n world!")
# print("hello \\n world!")
# print(r"hello \n world!")


# 常用函数
# 注意：一定要记住可变数据类型和不可变数据类型
# raplace 替换函数，将数组中old元素替换成new元素
# str1 = "abcdefghhhhhhh"
# str2 = str1.replace("h","a")
# print(id(str1),id(str2))
# print(str2)

# split([x],[y]) 将字符串按x进行分割,进行y次分割，分割得到一个列表数据
# str1 = "a,b,c,d,e,f,g,h,h"
# print(str1.split(",",4))
# # rsplit 与split相反
# print(str1.rsplit(",",4))

# x.join 以字符x将序列连接成一个新的字符串
# print("_".join(['a','b','c']))

# str.strip 截取字符串两边的空格或指定字符
#
# str1 = "        hello world         "
# print(str1.strip())
# print(str1.lstrip())
# print(str1.rstrip())

# str.removerefix() 截取字符串指定前缀
# str1 = 'hello'
# print(str1.removeprefix('he'))
# # str.removersuffix() 截取字符串指定后缀
# print(str1.removesuffix('lo'))

# str.lower() 所有字符转化为小写
# str.upper() 所有字符转化为大写
# str1 = 'hello'
# print(str1.upper().lower())

# str.swapcase() 将字符串的字符反转大小写
# str1 = 'hElLo'
# print(str1.swapcase())
# str.capitalize() 将字符串的第一个字符改为大写其他改为小写
# str1 = 'hElLo'
# print(str1.capitalize())

str1 = "hello world"
# find() 返回字符串中第一个x的索引值，不存在返回-1
# print(str1.find('e'))
# rfind() 与find()类似，只不过从右边查找，返回的索引都是从左往右，没有区别
# print("abcdefg".find('b'))
# print("abcdefg".rfind('b'))

# index() 返回字符串中第一个x的索引值，不存在报错
# print(str1.index('z'))

# count() 返回字符串中指定字符的个数
# print(str1.count('l'))

# str.startswith 检查字符串是否以x开头，可指定字符串开始结束范围
# print(str1.startswith("hzllo"))
# str.endswith 检查字符串是否以x结尾，可指定字符串开始结束范围
# print(str1.endswith("ld"))



str1 = "abc123"
# isalnum()判断字符串是否非空且只包含数字+字母（英文字母+汉字）的组合
print(str1.isalnum())
# isalpha()判断字符串是否非空且只包含字母（英文字母+汉字）的组合
print(str1.isalpha())
# isascii()判断字符串是否只包含ascii字符
print(str1.isascii())
# isdecimal()判断字符串是否非空且只包含十进制字符
print(str1.isdecimal())
# isdigit()判断字符串是否非空且只包含数字
print(str1.isdigit())
# isidentifier()判断字符串是否是有效标识符
print(str1.isidentifier())

