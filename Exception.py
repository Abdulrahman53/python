#=================================الاستثناءات
# try:
#     with open('my_file.txt','w') as file:
#         x=4
#         y=5
#         result=(x+y)/(x-y)
#         file.write(f'the result is:{result}')
# except FileNotFoundError as error:
#     print(error)
# except ZeroDivisionError as error:
#     print( error)
# else:
#     print(' done')
#===============================انشاء استثناء خاص بك
# class ToOld(Exception):
#     def __str__(self):
#         return "sorry you are old man"
# class ToYong(Exception):
#     def __str__(self):
#         return "sorry you are yong man"
# age= int(input('enter your age'))
# if age>45: raise ToOld
# if age <15: raise ToYong

