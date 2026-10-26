# 案例：人生目前处于那个阶段


from random import randint

age = randint(0,100)
print(f"当前年龄是{age}")

if age < 2:
    print("目前属于婴儿阶段")
elif age<4:
    print("目前属于幼儿阶段")
elif age<13:
    print("目前属于儿童阶段")
elif age<20:
    print("目前属于青少年阶段")
elif age<65:
    print("目前属于成年人阶段")
else:
    print("目前属于老年阶段")