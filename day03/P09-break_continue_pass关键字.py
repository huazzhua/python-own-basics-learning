# 打印0-9 偶数跳过
#
# for i in range(0,10):
#     if i % 2 == 0:
#         continue # 跳出当前循环
#     print(i)

# 案例 求0-9每个数自己幂自己的加和，如果大于10000000终止循环
sum = 0
for i in range(10):
    sum = sum + i**i
    print(f"第{i+1}次循环的加和为{sum}")
    if sum > 10000000:
        break

