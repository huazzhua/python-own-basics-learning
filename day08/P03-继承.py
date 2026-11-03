"""
    该案例演示了继承
"""
class Person:
    # 类属性
    home = "earth"
    def __init__(self, name):
        # 实例属性
        self.name = name

    def eat(self):
        print("eating")

class YellowRace(Person):
    color = "yellow"

class WhiteRace(Person):
    """白种人"""
    color = "white"  # 定义类属性

class BlackRace(Person):
    """黑种人"""
    color = "black"  # 定义类属性

y1 = YellowRace("y1")
print(y1.color,y1.name,y1.home)
y1.eat()

print("~~~~~~~")
w1 = WhiteRace("w1")
print(w1.color,w1.name,w1.home)
w1.eat()