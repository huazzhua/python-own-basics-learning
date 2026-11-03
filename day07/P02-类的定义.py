"""
    该案例演示了类的定义
"""
# 定义一个类
class Person:
    # 属性-- 类属性(所有类创建出来的对象共用该属性）
    home = "earth"

    # 方法
    def __int__(self,name,age):
        # 属性 -- 实例属性(每一个类创建的对象独有的)
        self.name = name
        self.age = age

    def eat(self):
        print("eating!")

    def drink(self):
        print("drinking!")

