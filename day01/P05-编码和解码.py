
# 注意: 如果编码和解码过程出现错误，一定是编码表的错误，解码和编码必须使用相同的编码表
str1 = "你好中国"
print(str1)
# 编码: 将字符串转化为字节的过程
b1 = str1.encode(encoding='gbk')
print(b1)
print(type(b1))
print("=======================")
# 解码: 将字节数据转化为字符串的过程，解码默认使用utf-8
str2 = b1.decode(encoding='gbk')
print(str2)
