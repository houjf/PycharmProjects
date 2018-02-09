# class Parent:
#     def pprt(self):
#         print(self)
#
# class Child(Parent):
#     c = 12
#     def cprt(self):
#         print(self)

# c = Child()
# c.pprt()
# c.cprt()
# p = Parent()
# p.pprt()

# import keyword
#
# a = keyword.kwlist
# print(len(a))
# print(keyword.iskeyword('has'))
# print(keyword.iskeyword('and'))
# print(c is a)

# a, b = 2, 3
import math

# def add(x, y, f):
#     return f(x)+ f(y)
#
# print(add(2, 5, math.sqrt))

# def f(x):
#     return x*2
#
# print (map(f, [1, 2, 5, 8]))

# for i in range(4,16,3):
#     print(i,end='')

for i in range(0, 10):
    if i<3:
        print("loop",i)
    else:
        continue
    print("heheeheh")