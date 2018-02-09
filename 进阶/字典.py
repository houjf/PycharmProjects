# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s, %s'%(self.__name, self.__score))
#
#     def get_grade(self):
#         if self.__score > 90:
#             return print('A')
#         elif 90 > self.__score > 80:
#             return print('B')
#         elif 80 > self.__score > 60:
#             return print('C')
#         else:
#             print('C')
#
# student = Student('hello', 60)
# student.print_score()
# student.get_grade()
# print(student.__name)
# n = student.__score
# print(n)

add = lambda x,y:x*y
b=add(2,6)
print(b)