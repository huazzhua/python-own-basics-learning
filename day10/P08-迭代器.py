"""
    可迭代的以及迭代器
"""
"""
import os

for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {"one": 1, "two": 2}:
    print(key)

for char in "123":
    print(char)

with open("myfile.txt", "w") as f:
    f.write("H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n")
for line in open("myfile.txt"):
    print(line, end="")
os.remove("myfile.txt")
var1 = (i for i in range(5))
# print(var1,type(var1))

for i in var1:
    print(i)
"""

"""
# 判断对象是不是可迭代的   Iterable
from collections.abc import Iterable

print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance(set(), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance("100", Iterable))  # True
print(isinstance(100, Iterable))  # False
"""
"""
# 判断对象是不是迭代器   Iterator
from collections.abc import Iterator

print(isinstance([], Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance(set(), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance("100", Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True
"""
"""
list1 = [1, 2, 3]
# for item in list1:
#     print(item)

# 返回迭代器对象
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
"""
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]

it = Reverse([1,2,3,4,5])
for item in it:
    print(item)

from collections.abc import Iterator
# list1 = [1, 2, 3,4,5]
# print(isinstance(list1,Iterator))
# it = iter(Reverse(list1))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
