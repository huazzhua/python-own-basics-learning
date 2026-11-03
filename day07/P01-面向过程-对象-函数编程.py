"""
    该案例演示了面向过程-对象-函数编程
"""


# ~~~~~~~~~~面向过程~~~~~~~~~~

# def 洗(name):
#     print(f"洗{name}")
# def 切(name):
#     print(f"切{name}")
# def 拌(*name):
#     print(f"拌{name}")
#
# def 上菜(name):
#     print(f"{name}上桌!!!")
# def 炸(name):
#     print(f"炸{name}")
# def 炖(*name):
#     print(f"炖{name}")
#
# 洗("黄瓜")
# 切("黄瓜")
# 拌("黄瓜","拉皮")
# 上菜("东北大拉皮")
#
# 洗("肉")
# 炸("肉")
# 上菜("锅包肉")
#
# 洗("茄子")
# 洗("豆角")
# 洗("土豆")
# 切("茄子")
# 切("豆角")
# 切("土豆")
# 炖("茄子","豆角","土豆","排骨")
# 上菜("东北大乱炖")

# ~~~~~~~~~~面向对象~~~~~~~~~~
# class 菜:
#     def __init__(self,name):
#         self.name = name
#
#     def 洗(self,czm):
#         print(f"洗{czm}")
#     def 切(self,czm):
#         print(f"切{czm}")
#     def 拌(self,*czm):
#         print(f"拌{czm}")
#
#     def 上菜(self,czm):
#         print(f"{self.name}上桌!!!")
#     def 炸(self,czm):
#         print(f"炸{czm}")
#     def 炖(self,czm):
#         print(f"炖{czm}")
#
# dlp = 菜("东北大拉皮")
# dlp.洗("黄瓜")
# dlp.切("黄瓜")
# dlp.拌("黄瓜","拉皮")
# dlp.上菜()


# ~~~~~~~~~~面向函数~~~~~~~~~~


def 洗(name):
    print(f"洗{name}")
def 切(name):
    print(f"切{name}")
def 拌(*name):
    print(f"拌{name}")

def 上菜(name):
    print(f"{name}上桌!!!")


def 东北大拉皮(*funcs):
    for func in funcs:
        func()

东北大拉皮(洗,切,拌,上菜)



