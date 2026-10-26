# while 循环


# 案例

# week = 1
# rabbit = 2
# while week < 10:
#     week +=1
#     rabbit = rabbit + rabbit*2
#     print(f"第{week}周兔子有{rabbit}只")

# 案例打印进度条
# import time
#
# num = 1
# while num < 100:
#     print("\r"+f"="*num,end="")
#     num += 1
#     time.sleep(0.1)

# breek

week = 1
rabbit = 2
while week < 10:
    week +=1
    rabbit = rabbit + rabbit*2
    print(f"第{week}周兔子有{rabbit}只")
    if week == 5:
        break # breek 结束循环
else:
    print("数兔子，数完了!")

print("今天是学习循环的一天!")