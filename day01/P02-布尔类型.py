bool1 = True
bool2 = False
print(bool1,type(bool2))
# 在python3中，bool是int子类，True与False可以和数字类似
print(isinstance(bool1,bool))
print(isinstance(bool1,int))

print(bool1+100)
print(bool2+100)

print("================")
print(bool1==1)
print(bool1 is 1)