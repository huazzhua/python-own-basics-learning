#

# res = 10/2
# print(res)
# print("程序执行完毕!")

try:
    res = 10 / 0
    print(res)
    print("程序执行完毕!")
except:
    print("除数不能为零")