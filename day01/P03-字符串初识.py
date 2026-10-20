# 字符串可以使用''或者""

str1 = 'hello'
print(type(str1))

str2 = "world"
print(type(str2))

str3 = str1 + str2
print(str3)
# 要保证字符串原样输出必须使用三个引号括起来
str4 = ("""hello
world""")
print(str4)
# \ 可在行尾作为续行符
str5 = ("hello \
world")
print(str5)

# 常用的转义字符 \b退格 \n换行 \t横向制表符-tab \r回车 回到行首
str11 = "hello \" world"
print(str11)