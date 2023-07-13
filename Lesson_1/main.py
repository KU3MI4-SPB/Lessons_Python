# print(5)
# print(5, 8, 6)

# n = 1.89
# print(n)

# n = 'fddf'
# print(n)

# n = 5
# print(type(n))

# n = 'fd\'df'
# print(n)

# a = 5
# b = 5.89
# c = 'hello'

# print(f"{a} - {b} - {c}")

# a = 5
# b = 5.89
# c = 'hello'

# print("{} - {} - {}".format(a,b,c))

# print('Введите первое число: ')
# a = input()
# print(a)

# print('Введите первое число: ')
# a = input()
# b = input('Введите второе число: ')
# print(a)
# print(b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# v = 'dfadsa'
# v = int(v)

# print('Введите первое число: ')
# a = int(input())
# b = int(input('Введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))

# a = 1 > 4
# print(a) # False
# a = 1 < 4 and 5 > 2
# print(a) # True
# a = 1 == 2
# print(a) # False
# a = 1 != 2
# print(a) # True
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# a = 1 < 3 < 5 < 10
# print (a) # True

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит!')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2: 
#         print(n)
#         flag = False
#     i += 1

# for i in 1, -2, 3, 14, 5:
#     print(i)

# r = range(100, 0, -20)
# for i in r:
#     print(i)

# a = 'querty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) 
# print('ещё' in text)
# print(text.lower())
# print(text.upper()) 
# print(text.replace('ещё','ЕЩЁ')) 

text = 'съешь ещё этих мягких французских булок'
print(text[0])                           # c
print(text[1])                           # ъ
print(text[len(text)-1])                 # к
print(text[-1])                          # к
print(text[-5])                          # б
print(text[:])                           # съешь ещё этих мягких французских булок
print(text[:2])                          # съ
print(text[len(text)-2:])                # ок
print(text[2:9])                         # ешь ещё
print(text[6:-18])                       # ещё этих мягких
print(text[0:len(text):6])               # сеикакл
print(text[::6])                         # сеикакл
text = text[2:9] + text[-5] + text[:2]   # ...
print(text)