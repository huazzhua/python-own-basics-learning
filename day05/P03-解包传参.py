# 解包传参

# def func(a,b,c):
#     print(a,b,c)
#
# # tup1 = (1,2,3)
# # func(*tup1)
#
# dict1 ={"a":1,"b":3,"c":2}
# func(**dict1)


# 强制使用位置参数或者关键字参数   /前的参数必须使用位置参数，*后的参数必须使用关键字参数

def func(a,b,/,c,d,e,*,f,g):
    print(a,b,c,d,e,f,g)

func(1,2,3,4,5,f=6,g=7)