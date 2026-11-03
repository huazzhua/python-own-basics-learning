"""
    该案例演示了self
"""
class Student:
    # 类属性
    school = "atguigu"

    def __init__(self,name,age):
        # 实例属性
        self.name = name
        self.age = age

    def eat(self):
        print("eating")

    def 站着听(self):
        # self.eat()
        # Student.eat(self)
        print(f"年龄是{self.age}的小伙{self.name}正在站着听课")

xjq = Student("xjq",20)
print(xjq.name)
print(xjq.age)
xjq.站着听() #===>Student.站着听(xjq)
# print(Student.站着听)


