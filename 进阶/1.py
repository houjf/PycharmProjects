
# f = abs()
# def add(x, y, f):
#     return  f(x)+f(y)
#
# print(add(-2,4,abs))

# def f1(x):
#     return x*2
#
# def new_fn(f):
#     def fn(x):
#         print('call'+f.__name__+'()')
#         return f(x)
#     return fn
#
# @new_fn
# def f2(x):
#     return x*2
# print(f2(2))

import re
import os
import time

def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path)
        lists = file_path.split('.')
        file_ext = lists[-1]
        img_ext = ['bmp', 'jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0]+'/'+'_fc.'+file_ext)
            i+=1
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x))

img_dir = 'E:\\03_dbimages'
img_dir = img_dir.replace('\\', '/')
# print(img_dir)
# start = time.time()
# print(start)
# print(os.path.isdir(img_dir))
print(os.path.isfile(img_dir+'/1a2cb0ba3841eda.jpg'))
# print(os.listdir(img_dir))
# for x in os.listdir(img_dir):
#     c = img_dir+'/'+x
    # print(c)
    # print(os.path.join(img_dir,x))

# i = 0

t = img_dir+'/063bb07a807a340.jpg'
# p = os.path.split(t)
# print(p)
# img_h = p[-1]
# print(img_h)
# h = img_h.split('.')
# print(h)
# if h[-1] in ['bmp', 'jpeg','gif','psd','png','jpg']:
#     print('该文件为图片')
#     # u = os.rename(t, p[0]+'/'+'_fy'+img_h)
#     print(os.getcwd())

# print(os.system('ping huangwq-pc1'))
# print(os.putenv('path', 'C:\\EFI'))
# print(os.getenv('path'))

# print(os.path.getsize(t))
# print(os.stat(t))
# d = os.stat(t).st_size
# print(d)
os.getcwd()
# os.mkdir('test')
l = os.getcwd()+'\\test'
print(l)
# os.system('cd %s'%(l))
# os.system('ls')
os.mknod("test.txt")

