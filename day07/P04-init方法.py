class Person:
    """类说明文档--人的类"""
    # 属性-- 类属性(所有类创建出来的对象共用该属性）
    home = "earth"


    def __new__(cls, *args, **kwargs):
        print("new方法被调用了！")
        return object.__new__(cls)

    # 方法
    def __init__(self,name,age):
        # 属性 -- 实例属性(每一个类创建的对象独有的)
        self.name = name
        self.age = age

    def eat(self):
        print("eating!")

    def drink(self):
        print("drinking!")