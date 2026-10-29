"""
    该案例演示了文件的读写操作
"""

# 向磁盘文件中写入数据
# # 建立连接(通过open方法打开文件)
# f = open("test.txt","w")
#
# # 写入数据
# f.write("hello world!\n")
# f.write("你好python！\n")
# # 关闭连接
# f.close()

# 向磁盘文件中读取数据
# 建立连接(通过open方法打开文件)
f = open("test.txt","rt")

# 读取数据  --read()
# read() 没有加任何参数，表示读取文件中所有内容
# read(size)  如果加参数，表示从文件中读取的字节数
# print(f.read())
# print(f.read(5))
# print(f.read(8))

# 读取数据  --readline()
# print(f.readline(5))    # --读取一行数据

# 读取数据
print(f.readlines())

# 关闭连接
f.close()














