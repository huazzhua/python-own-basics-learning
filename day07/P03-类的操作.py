"""
    该案例演示了类的操作
"""


class Person:
    """类说明文档--人的类"""
    # 属性-- 类属性(所有类创建出来的对象共用该属性）
    home = "earth"

    # 方法
    def __init__(self,name,age):
        # 属性 -- 实例属性(每一个类创建的对象独有的)
        self.name = name
        self.age = age

    def eat(self):
        print("eating!")

    def drink(self):
        print("drinking!")

# 类操作 -- 成员引用

# home = Person.home
# eating = Person.eat
# print(eating)
# doc = Person.__doc__
# print(doc)


# 类操作 -- 实例化

zhangsan = Person(name='zs',age = 23)
zhangsan.eat()
zhangsan.drink()
print(zhangsan.home)