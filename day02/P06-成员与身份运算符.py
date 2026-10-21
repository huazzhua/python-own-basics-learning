# 成员运算符
# in，在指定序列中找到值，返回True,反之返回false
# not in 在指定序列中找到值，返回True,反之返回false
list = [1,2,3]
print(1 in list)
print(11 in list)

# 身份运算符
n = 20
m = 20
q = 30

print(n is m)
print(n is q)
print(n is not q)
print(id(n) is id(m))