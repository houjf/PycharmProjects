# p = (4, 5)
# x, y = p
# print(x,y)

# data = ['ACME', 50, 91.2, (2012, 6, 19)]
# x, y, z, t = data
# print(x, y, z, t)

# s = 'hello'
# x, y, z, t, p = s
# print(x, y, z, t, p)

# s = {1, 2, '12',(2,4)}
# x, y, z, t = s
# print(x, y, z, t)

# s = {1:'hello', 2:'up', 3:'om'}
# x, y, _ = s
# print(x,y,_)

# s = [90, 80, 70, 60, 45]
# import math
# def drop_first_last(grades):
#     fist, *middle, last = grades
#     return middle
#
# def drop_first(grades):
#     first, *lates = grades
#     return lates
#
# def drop_last(grades):
#     *leaders, last = grades
#     return leaders
#
# print(drop_first_last(s))
# print(drop_first(s))
# print(drop_last(s))

# s = ['ACME', 50, 91.2, (2012, 6, 19)]
# name, *_,(*_, ri) = s
# print(name, ri)

# s = ['ACME', 50, 91.2, (2012, 6, 19)]
# (a), *_,(*_, ri) = s
# print((a))

import cmath
# s = [90, 80, 70, 60, 45]
# def last_sum(ma):
#     head, *last = ma
#     return head+sum(last)
# print(last_sum(s))

# import heapq
# nums = [1,8,2,23,7,-4,18,23,42,37,2]
# print(heapq.nlargest(3,nums))
# print(heapq.nsmallest(2,nums))
# heap = list(nums)
# heapq.heapify(heap)
# print(heap)
# print(heap[0])
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heap)
# print(min(nums))
# print(max(nums))
# print(sorted(nums))

# from collections import OrderedDict
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4
# print(d)
# for key in d:
#     print(key,d[key])

# prices = {'ACME':45.23,'AAPLE':612.78,'IBM':205.55,'HPQ':37.2,'FB':10.75}
# d = zip(prices.values(),prices.keys())
# print(d)
# print(min(d))
# print(sorted(d))

# print(zip([1],[4]))
# a = {'x':1,'y':2,'z':3}
# b = {'x':10,'y':2,'w':13}
#
# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(a.items() & b.items())

# import re
#
# data = b'FOO:BAR,SPAM'
# d = re.split(b'[:,]',data)
# print(data.decode('ascii'))

# filename = "spam.txt"
# print(filename.endswith('.txt'))
# print(filename.startswith('file'))
# print(filename.startswith('spam'))
# print(filename.startswith('pam'))

# import os
#
# filename = os.listdir()
# print(filename)
# data = [name for name in filename if name.endswith(('.py', '.jpg'))]
# print(data)

# import requests

# def read_data(name):
#     if name.startswith(('http','https','ftp')):
#         return open(name).read()
#     else:
#         with open(name) as f:
#             return f.read()

# print(tuple({1:'23'}))

# import re
# t1 = '11/27/2012'
# t3 = 'w/e/rt'
# t2 = 'now 27, 2012'
# if re.match(r'\a+/\a+/\a+',t3):
#     print('yes')
# else:
#     print('no')

# t1 = 'jdshdhiofbjbbjbgjfojoijoii'
# print(t1.replace('i', 'x'))

import re
# t1 = '11/27/2012'
# re.findall()
# print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2',t1))

# text = 'UPPER PYTHON, lower python, Mixed Python'
#
# print(re.findall('python',text,re.IGNORECASE))
# print(re.findall('python', text))

# str_pat = re.compile(r'\"(.*?)\"')
# text = 'Computer says "no." PHONE says "yes"'
# d=str_pat.findall(text)
# print(d)

# t = '---=---hello=====-'
# print(t.strip('-'))
# print(t.lstrip('-'))
# print(t.rstrip('-'))
# print(t)

# s = 'pýtĥöñ\fis\tawesome\r\n'
# remap = {ord('\t') : ' ',ord('\f') : ' ',ord('\r') : None }
# print(s.translate(remap))

# t = "hello word"
# print(t.ljust(20))
# print(t.rjust(20, '-'))
# print(t.center(20, '*'))

# print(round(3331.289,-2))


# x = 123456
# print(bin(x))
# print(oct(x))
# print(hex(x))


# import fractions
# a= fractions.Fraction(5,4)
# print(a.numerator)
# print(a.denominator)

# import numpy as np

# a= np.array([1,2,3,4])
# b = np.array([2,3,5,6])
# print(a+1)
# print(a**2)
# print(a*b)
# print(np.sqrt(a))

# grid = np.zeros((5,5),int)
# print(grid+4)
# print(np.sqrt(grid+4))

items = [2,5,8,9]
it = iter(items)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))













