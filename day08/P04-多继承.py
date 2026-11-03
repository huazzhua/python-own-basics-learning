"""
    该案例演示了多继承
"""
class Person:
    home = "earth"
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("eating...")

class YellowRace(Person):
    color = "yellow"
    def run(self):
        print("run...")

class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print("study...")

class ChineseStudent(Person,YellowRace,Student):
    country = "中国"

zs = ChineseStudent("zs")

# zs = ChineseStudent("zs","1年级")
# print(zs.country,zs.name,zs.grade,zs.color,zs.home)
#
# zs.study()
# zs.run()
# zs.eat()




