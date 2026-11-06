# 不同类型的异常可以有不同的处理方式
try:
    # res = 10 / 0
    # print(res)
    print("a" +10)
except ZeroDivisionError as e:
    print("除数不能为0")
except NameError as e:
    print("变量名未定义")
except TypeError as e:
    print("类型有问题")
except (NameError,TypeError) as e:
    print(e)
except:
    print("other error")


# try:
#     # 可能发生异常的代码
#     res = 10 / 1
# except:
#     # 如果发生异常，对异常进行处理的代码
#     print("除数不能为0")
# else:
#     # 如果try中代码没有发生异常，将执行 else 中的代码
#     print(res)