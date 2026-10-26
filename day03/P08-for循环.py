# for 循环
# 遍历列表
# for i in [10,20,30,40,50]:
#     print(i)
#
# # 遍历字符串
# for i in "hello world!":
#     print(i)

# 遍历range数列
# var = range(10)
# print(type(var))
#
# for i in range(1,10):            # range(x,y)包含起始不包含结束
#     print(i)


# 案例九九乘法表

for i in range(1,10):
    for j in range(1,i+i):
        print(f"{i}*{j}={i*j}",end="  ")
    print("",end="\n")