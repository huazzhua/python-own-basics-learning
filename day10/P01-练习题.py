"""
    该案例讲解了晨测题
"""
"""
# 编写一段 Python 代码，尝试将字符串 "123abc" 转换为整数，如果转换失败，捕获 ValueError 异常，
# 将异常信息记录到一个文本文件 error.log 中

try:
    num = int("123abc")
except ValueError as e:
    with open("error.txt", "w") as file:
        file.write(str(e))
"""

# 定义一个函数check_age，该函数接受一个年龄参数。如果年龄小于 0，抛出一个自定义异常InvalidAgeError；
# 如果年龄大于 120，抛出UnrealisticAgeError。
# 这两个自定义异常类都继承自Exception类。调用该函数并传入一个不合法的年龄值，捕获并处理异常。

class InvalidAgeError(Exception):
    pass

class UnrealisticAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def check_age(age):
    if age < 0:
        raise InvalidAgeError("年龄不能小于0")
    elif age > 120:
        raise UnrealisticAgeError("年龄不能大于120")
    else:
        print("正常年龄范围")



try:
    check_age(-8)
except (InvalidAgeError,UnrealisticAgeError) as e:
    # print(e)
    pass










