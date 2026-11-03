"""
    该案例演示了方法的解析顺序MRO
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
        Person.eat(self)
        print("studying...")

class ChineseStudent(YellowRace,Student):
    """中国学生"""

    country = "中国"

y1 = ChineseStudent("张三", "三年级")

print(ChineseStudent.__mro__)