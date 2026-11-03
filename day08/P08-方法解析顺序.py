
"""
class A:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
class B:
    def __init__(self, d,e,f):
        self.d = d
        self.e = e
        self.f = f

class C(A,B):
    def __init__(self, a,b,c,d,e,f):
        pass
        # A.__init__(self,a,b,c)
        # B.__init__(self,d,e,f)
        # super().__init__(a,b,c)
        # super(A,self).__init__(d,e,f)

"""


"""
class Parent1:
    def __init__(self, value1):
        print("Initializing Parent1")
        self.value1 = value1

class Parent2:
    def __init__(self, value2):
        print("Initializing Parent2")
        self.value2 = value2


class Child(Parent1, Parent2):
    def __init__(self, value1, value2):
        print("Initializing Child")
        # 调用 Parent1 的 __init__ 方法
        super().__init__(value1)
        # 调用 Parent2 的 __init__ 方法   Parent1 之后开始查找 MRO 链，调用下一个父类（即 Parent2）的 __init__ 方法，把 value2 传递进去。
        super(Parent1, self).__init__(value2)
        # super().__init__(value2)

print(Child.__mro__)
child = Child("value from Parent1", "value from Parent2")
print(child.value1)
print(child.value2)

"""

class Parent1:
    def __init__(self, value1, **kwargs):
        print("Initializing Parent1")
        super().__init__(**kwargs)
        self.value1 = value1


class Parent2:
    def __init__(self, value2, **kwargs):
        print("Initializing Parent2")
        super().__init__(**kwargs)
        self.value2 = value2


class Child(Parent2, Parent1):
    def __init__(self, value1, value2):
        print("Initializing Child")
        super().__init__(value1=value1, value2=value2)

print(Child.__mro__)
child = Child("value from Parent1", "value from Parent2")
print(child.value1)  # 输出: value from Parent1
print(child.value2)  # 输出: value from Parent2
""""""

"""
class Parent1:
    def __init__(self, value1):
        print("Initializing Parent1")
        self.value1 = value1

class Parent2:
    def __init__(self, value2):
        print("Initializing Parent2")
        self.value2 = value2


class Child(Parent1, Parent2):
    def __init__(self, value1, value2):
        print("Initializing Child")
        # 直接调用 Parent1 的 __init__ 方法
        Parent1.__init__(self, value1)
        # 直接调用 Parent2 的 __init__ 方法
        Parent2.__init__(self, value2)


child = Child("value from Parent1", "value from Parent2")
print(child.value1)
print(child.value2)

"""

# 使用 super()：适用于遵循 MRO 顺序的场景，代码可维护性和扩展性较好，特别是在复杂的多重继承结构中。
# 直接调用父类方法：代码逻辑较为直观，但在多重继承结构发生变化时，可能需要手动调整调用顺序，可维护性较差。