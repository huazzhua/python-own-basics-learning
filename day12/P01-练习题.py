# import P01_math_operations   # 全局导入，导入当前模块下的所有成员
#
# print(P01_math_operations.add(1, 2))
# print(P01_math_operations.mul(2, 3))


# from P01_math_operations import * # 局部导入,导入所有不以下划线开头的成员
#
# print(add(1, 2))
# print(mul(2, 3))

# from P01_math_operations import add,mul  # 局部导入，导入具体的成员
# print(add(1, 2))
# print(mul(2, 3))


# 使用生成器表达式创建一个生成器
# gen = (i for i in range(1,11) if i % 2 == 0)
# for i in gen:
#     print(i)


# 创建一个迭代器类MyIterator，用于正序遍历一个给定列表的元素

class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.data[self.index]

it = MyIterator([10,20,30,40])
for i in it:
    print(i)

