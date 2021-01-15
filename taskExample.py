# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# hello = "Hello"
# result = hello +", "+ name + " " + surname + "!"
# print(result)



""" вычисление факториала  с циклом while """
# number = int(input("Введите число: "))
# i = 1
# factorial = 1
# while i <= number:
#     factorial *= i    
#     i += 1
#     print(i , factorial)
# print("Факториал числа", number, "равен", factorial)



""" Программа по вычислению факториала c  for""" 
# number = int(input("Введите число: "))
# factorial = 1
# for i in range(1, number+1):
#     factorial *= i    
# print("Факториал числа", number, "равен", factorial)



# words = input("Введи несколько слов: ")
# words = words.split()
# newList = list()
# for word in words:
#     if word[0] == "q":
#         newList.__add__(word)
#     print(word)
# print(newList)        



"""
Практика над множествами
"""

# создание множества
# list_ = [1,2,3,4,5,6]
# set_ = set(list_)
# print(type(set_))


# list_ = ['Koly','Sasha','Toly']
# list_2 = ['Koly', 'Aibek','Bek']
# set_ = set(list_)
# set_2 = set(list_2)

# unique_ = set.union(set_,set_2)

# intersection_ = set.intersection(set_,set_2)

# difference_ = set.difference(set_,set_2)

# len_ = len(unique_)

# unique_.add('Gairat')

# unique_.remove('Koly')

# unique_.discard('Toly')

# unique_.pop()

# unique_.clear()

# unique_ = set_.copy()

# isbool = set_.isdisjoint(set_2)

# issuperset_ = set_.issuperset(set_2)

# result = set_2.difference(set_)

# print(result)



"""
найти сумму трех значного числа
"""

# number = input('Введи трехзначное число: ')

# i = 0
# for num in number:
#     num = int(num)
#     i += num
# print(i)


'''
таблица умножения через while
'''

# i = 1
# while 10 > i:
#     j = 1
#     while 10 > j:
#         result = i * j        
#         print(result, end='\t' if j < 9 else '\n')
#         j +=1
#     i += 1
    


"""
изменить порядок цифр на обратный
"""






"""
доп задачи
"""


#1
"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

# list_ = [
#          i for i in range(1,1000)
#          if i % 3 ==0 or i % 5 ==0
#         ]
# print(sum(list_))




#2
'''
 Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона. 
'''
# list_num = [1,2]
# example_num = 0
# while example_num < 4000000:
#     example_num = list_num[-2] + list_num[-1]
#     if example_num < 4000000:
#         list_num.append(example_num)
#     print(list_num)    
    
# list_num = [i for i in list_num if i % 2 == 0]

# print(f'сумма всех четных элементов ряда Фибоначчи,\
#  которые не превышают четыре миллиона, ровна {sum(list_num)}')




#3
# number = 600851475143
# list_ = [print(i) for i in range(2, number + 1) if i % i == 0 and i % 1 ==0 and i % 2 != 0 and i % 3 != 0 or i == 2 or i == 3]
# print(list_)


# number = 600851475143
# list_ = []
# result = 0
# for i in range(2, number + 1):
#     if i % i == 0 and i % 1 ==0 and i % 2 != 0 and i % 3 != 0 or i == 2 or i == 3:
#         list_.append(i)
# print(max(list_))


#4

"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

"""
# list_ = []
# for i in range(100,1000):
#     for j in range(100,1000):
#         first = str(i * j)
#         second = int(first[::-1])
#         if int(first) == second:
#             list_.append(first)

# print(max(list_))



#5
'''
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''

# list_ = [i for i in range(1,1000000) for j in range(1,21)  if i % j == 0]
# print(list_)


# list_ = []
# for i in range(1,10000):
#     count_ = []
    
#     for j in range(1,11):
#         if i % j == 0:
#             count_.append(1)
            
#     if len(count_) == 10:
#         list_.append(i)

# print(min(list_))



# вопросы к интерактиву
# 1. что такое итерация ?
# 2. в чем разница между тренарным оператором и условными операторами
# 3. в каких случаях работает else?
# 4. можно ли внутри условных операторов создавать  несколько циклов 
# 5. Принцып работы while и for и в чем из разница






#6
# Сумма квадратов первых десяти натуральных чисел равна
# 12 + 22 + ... + 102 = 385

# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)2 = 552 = 3025

# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

# first = sum([i ** 2 for i in range(1,101)])
# second = [i for i in range(1,101)]
# print(pow(sum(second),2) - first)





#7


# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

# Какое число является 10001-ым простым числом?

# list_num = [i for i in  range(1,1000000) if i % i == 0 and i % 1 == 0 and i % 2 != 0 and i % 3 != 0 or i == 2 or i == 3]
# print(list_num[10000]) # индекс начинается с 0. так что 10001 число будет лежать под 10000 индексом




#9
# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a2 + b2 = c2

# Например, 32 + 42 = 9 + 16 = 25 = 52.

# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

# for i in range(1,25):
#     num_1 = i ** 2
#     for j in range(1,25):
#         num_2 = j ** 2
#         for f in range(1,25):
#             num_3 = f ** 2
#             num = num_1 + num_2 + num_3  
#             if num == 1000:
#                 print(f'{num_1}\n{num_2}\n{num_3}\n{num}')
#                 break



#10
# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

# Найдите сумму всех простых чисел меньше двух миллионов.

# sum_num = [i for i in range(2,11) if i % i == 0 and i % 1 ==0 and i % 2 != 0 and i % 3 != 0 or i == 2 or i == 3]
# print(sum(sum_num))




#12 

# Последовательность треугольных чисел образуется путем сложения натуральных чисел. К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Перечислим делители первых семи треугольных чисел:

#      1: 1
#      3: 1, 3
#      6: 1, 2, 3, 6
#     10: 1, 2, 5, 10
#     15: 1, 3, 5, 15
#     21: 1, 3, 7, 21
#     28: 1, 2, 4, 7, 14, 28 

# Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

# Каково первое треугольное число, у которого более пятисот делителей?



# list_num = []
# list_i = []
# for i in range(1,100):
#     list_i.append(i)
#     if len(list_i) > 0:
#         list_num.append(sum(list_i))
    
#     if list_num[-1] == 28:
#         break
# print(list_num)


# count_ = []
# for i in enumerate(list_num):
#     print(f'{i[1]}:', end='\t')
#     for j in range(1,list_num[i[0]] + 1):
#         if i[1] % j == 0:
#             print(f'{j}', end=',\t' if j < list_num[i[0]] else '\n')
           
    


#13

# count_ = 0
# list_count = []
# # for i in enumerate(range(1,14)):
# n = 13
# while True:
#     if n == 2 :
#         n /= 2
#         count_ += 1
#         list_count.append(i)
#         print(int(n))
#         break
#     elif n % 2 != 0:
#         n = n * 3 + 1
#         count_ += 1
#         print(f'{int(n)} -->', end=' ')
#     else:
#         n /=2
#         count_ += 1
#         print(f'{int(n)} --> ', end=' ')





#16 

# num = 2 ** 1000

# list_num = [int(i) for i in str(num)]
# print(sum(list_num))


#20

# list_ =[]
# for i in range(1,10):
#     if not len(list_):
#         list_.append(i * (i + 1))
#     else:
#         list_.append(list_[-1] * (i + 1) )

# num = [int(i) for i in str(list_[-1])]
# print(sum(num))


# #21
# num = 222
# list_ = [i for i in range(1,num ) if num % i == 0]
# print(sum(list_))


