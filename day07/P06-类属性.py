"""
    该案例演示了属性
"""
# 类属性
class Person:
    """人的类"""
    home = "earth"  # 定义类属性
    # pass

# 通过类名.属性名方式访问
# print(Person.home)

# 通过实例名.属性名方式访问
# zs = Person()
# print(zs.home)
# ls = Person()
# print(ls.home)


# print(Person.home)
# Person.home = "地球"
# print(Person.home)


zs = Person()
zs.home = "地球"
print(zs.home)

ls = Person()
print(ls.home)