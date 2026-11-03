"""
    该案例演示了super访问父类中的成员
"""
class Person:
    """人的类"""

    home = "earth"

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")


class YellowRace(Person):
    """黄种人"""

    color = "yellow"

    def run(self):
        print("runing...")

class Student(Person):
    """学生"""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("先吃再学")
        # 调用父类中的eat方法
        # Person.eat(self)
        # self.eat() # =>Person.eat(self)
        # super().eat()
        print(super().home)
        print("studying...")

zs = Student("zs","1年级")
zs.eat()
zs.study()
