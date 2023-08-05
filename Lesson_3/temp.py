# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input('Введите число N: '))

# print(fib(n))

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# def replace_scores(scores):
#     max_score = scores[0]
#     min_score = scores[0]
#     for score in scores:
#         if score > max_score:
#             max_score = score
#         if score < min_score:
#             min_score = score
#     replaced_scores = []
#     for score in scores:
#         if score == max_score:
#             replaced_scores.append(min_score)
#         else:
#             replaced_scores.append(score)
#     return replaced_scores

# n = int(input("Введите количество оценок: "))
# scores = []
# for i in range(n):
#     score = int(input("Введите оценку: "))
#     scores.append(score)
    
# replaced_scores = replace_scores(scores)

# print('Исправленные оценки:', end=" ")

# for score in replaced_scores:
#     print(score, end=" ")

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# def easy_num(n):
#     if n == 1:
#         return('Нет')
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return('Нет')
#     return('Да')
    
# n = int(input('Введите число: '))
# print(easy_num(n))

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Например: 
# Введите число N:
# Input: 5
# Изначальные элементы: 12 13 14 15 16
# Элементы в обратном порядке: 16 15 14 13 12

def reverse_num(n):
    if n == 0:
        return
    x = int(input())  
    reverse_num(n - 1) 
    print(x, end=' ')  
    
n = int(input('Введите число N: '))

print(f'Введите последовательно {n} элементов: ', end='')
reverse_num(n)