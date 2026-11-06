# def a_add(num1,num2):
#     return num1+num2
# def b_add(num1,num2):
#     a_add(num1,num2)
#
# # 注意此处打印无任何值，因为b_add()方法，在调用a_add()方法是没有做接收，故没有返回任何值，如果要返回，应该这样写
# # def b_add(num1,num2):
# #     sum = a_add(num1,num2)
# #     return sum
# print(b_add(1, 2))



# 练习题1：动态添加属性
# class Person:
#     pass
#
#
# std = Person()
# std.hobby = "reading"
# print(std.hobby)

# 练习题2：动态添加方法
# import types
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#
# def calculate_area(self):
#     return 3.14 * self.radius * 2
#
# cle = circle(5)
# # 为类添加实例方法
# cle.calculate_area = types.MethodType(calculate_area,cle)
# print(cle.calculate_area())

# 练习题3：封装特性

# class BankAccout:
#     def __init__(self):
#         self.__balance = 0
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self,amount):
#         self.__balance = amount
    # def deposit(self,money):
    #         self.__balance =money
    # def withdraw(self,money):
    #     if money > self.__balance:
    #         print("余额不足")
    #     else:
    #         self.__balance -= money
    #         print(f"余额还有{self.__balance}")

# people = BankAccout()
# people.deposit(100)
# people.withdraw(30)
# print(people.balance)
# people.balance = 100
# print(people.balance)


# 多态特性

class shape:
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height= height
    # 父类方法重写
    def area(self):
        return self.width * self.height
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius

    # 方法重写
    def area(self):
        return 3.14 * self.radius * 2

list1 = [Rectangle(3,4),Circle(5)]

for i in list1:
    print(i.area())

