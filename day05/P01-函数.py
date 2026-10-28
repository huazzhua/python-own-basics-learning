# 案例一打印两行三列的星星

# rows = 2
# while rows > 0:
#     print("*"*3)
#     rows -= 1

# 封装打印两行三列的函数
# def print_start():
#     rows = 2
#     while rows > 0:
#         print("*"*3)
#         rows -= 1
#
# print_start()

# 封装带有参数的函数

def print_start_1(rows,cols):
        while rows > 0:
            print("*" * cols)
            rows -= 1

print_start_1(1,4)