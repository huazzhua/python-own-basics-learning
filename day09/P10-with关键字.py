"""
    该案例演示了with自动释放资源
"""
# try:
#     file = open("test.txt", "wt")
#     # print(type(file))
#     file.write(str1)
#     file.close()
# finally:
#     print("文件是否关闭",file.closed)

#
# try:
#     try:
#         file = open("test.txt", "wt")
#         # print(type(file))
#         file.write(str1)
#     finally:
#         file.close()
# finally:
#     print("文件是否关闭",file.closed)



try:
    with open("test.txt","wt") as file:
        file.write("hello world")
finally:
    print("文件是否关闭：", file.closed)