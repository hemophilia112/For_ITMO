year = int(input("Введите год "))
# Первый вариант:
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Високосный год ")
#         else:
#             print("Невисокосный год ")
#     else:
#         print("Високосный год ")
# else:
#     print("Невисокосный год ")
 
# Второй вариант:
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный год ")
else:
    print("Невисокосный год ")



