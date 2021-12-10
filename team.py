#         11
#
# user = input('Введите слово через пробел: ')
# words = user.split()
# q = " "
# for i in sorted(words,key=lambda a: len(a)):
#     q = q + " " + i
# print(q)
#
#         9
#
# User_Str = input('Enter your text\n')
# Index = 0
# Upper = 0
# Lower = 0
# try:
#   while True:
#     if User_Str[Index] == User_Str[Index].upper():
#       Upper += 1
#
#     else:
#       Lower += 1
#
#     Index += 1
# except:
#   print(len(User_Str),'words')
#   t = len(User_Str)/Upper
#   t1 = len(User_Str)/Lower
#   x = round(t,2)
#   print('Upper',x,' %')
#   x1 = round(t1,2)
#   print('Lower: ',x1, ' %')
#
#
#           1
# print(''.join(s for s in input().lower() if s not in 'aoyeui'))
#


# Задание 2:
# Вам дан набор данных accounts.
# Функция должна проходить по каждому листу состоящему из 3-х символов и
# найти ту
# где их сумма больше всего.

# accounts = [
#     [1,5,5],[7,4,5],[1,3,5],[2,1,5],[7,3,9],[8,3,5],[1,5,0],[7,3,2],[9,3,5],
#     [1,5,3],[2,7,3],[6,3,5],[1,5,9],[7,3,3],[3,5,4],[1,5,6],[7,3,6],[3,5,8],
#     [1,5,3],[7,3,0],[3,5,4],[1,5,6],[7,3,2],[3,5,4],[1,5,9],[7,3,2],[3,5,0],
#     [1,5,1],[7,3,2],[3,5,3],[1,5,4],[7,3,5],[3,5,6],[1,5,7],[7,3,8],[3,5,9],
# ]
# def largest_sum():
#     largest_sum = 0
#     for x in range(len(accounts)):
#         summa = sum(accounts[x])
#         if largest_sum < summa:
#             largest_sum = summa
#             largest_list = accounts[x]
#     return largest_sum, largest_list
# print('largest sum is: ', largest_sum())

################################################################################


# Задание 3:
# Вам даны 2 листа:

# list_1 = ['a', 'bc', 'de']
# list_2 = ['ab', 'c', 'de']

# Напишите функцию которая их принимает и сравнивает на равность.
# Пример где листы равны:

    # a + bc + de = abcde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['1', '23', 'abcde']

# Пример где листы НЕ равны:

    # a + cb + de = acbde
    # ab + c + de = abcde

    # list_1 = ['123', 'abc', 'de']
    # list_2 = ['123', 'de', 'abc']

# list_1 = ['a', 'bc', 'de']
# list_2 = ['ab', 'c', 'de']
# def cheak(list1, list2):
#     a = ''
#     b = ''
#     for x in range(len(list1)):
#         a += list1[x]
#         b += list2[x]
#     if a == b:
#         return 'Листы ровны'
# print(cheak(list_1,list_2))

################################################################################


# Задание 4:
# Известно что функция print() выводит на экран текст который Вы в ней указали.
# Известно что есть ещё один способ вывести на экран любой текст sys.stdout.write(), но его использовать нельзя.
# Так случилось что функция print поменяла своё имя и стала называться display.
# Выведите с помощью новой функции display() на экран следующий текст: "Теперь я тут PRINT()"
# Общее количество строк для решения этой задачи не может быть больше 2-х строк, иначе задание не принимается.
# display = lambda x: print(x)
# display('Теперь я тут PRINT()')



################################################################################


# Задание 5:
# Вам дан SET значений:

# uniques = {3,13,15,27,1,4,8,23,19,12,9,2,17}

# Создайте функцию которая:
# Удалите все чётные значения внутри SET, а оставшиеся отсортирует по убыванию.
# В результате, ваша функция должна вернуть отсортированный SET и неважно, каким будет SET растопленным или замороженным.

# uniques = {3,13,15,27,1,4,8,23,19,12,9,2,17}
# def sorting(set_1):
#     lst = []
#     for x in set_1:
#         if x % 2 == 0:
#             lst.append(x)
#     for y in lst:
#         set_1.remove(y)
#     return set_1
# print(sorting(uniques))

################################################################################


# Задание 6:
# В Python есть такой тип Данных как Boolean...
# Создайте TUPLE который ТЕХНИЧЕСКИ состоит из 4 Булевых ЗНАЧЕНИЙ.
# asd = (True,False,True,False)
################################################################################


# Задание 7:
# Вам дан TUPLE и пустая Dictionary:

# pairs = {}

# В Tuple перечислены элементы, где идёт строгая очерёдность STRING и INTEGER.
# То есть если перед вами элемент типа данных STRING то следующий точно INTEGER и наоборот.
# keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6 'six', 7, 'seven', 'eight', 8, 'nine',9, 10, 'ten', 11, '11', 12 ,'13')
# Проходя по TUPLE необходимо брать элементы по парно, один элемент может относиться только и только к одной паре.
# Ваша задача выявить если элемент является типом данных string() то записывать его как ключ в Dictionary -> pairs.


# Пример:
# pairs ={'one': 1, 'two': 2, 'three': 3, ...}
# import operator
# dick = dict()
# keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6, 'six', 7, 'seven', 'eight', 8, 'nine', 9, 10, 'ten', 11, '11', 12 ,'13')
# lst = list(keys_values)
# keys1 = []
# values1 = []
# for x in lst:
#     if type(x) == str:
#         keys1.append(x)
#     if type(x) == int:
#         values1.append(x)
# for x in range(len(keys1)):
#     element = {keys1[x] : values1[x]}
#     dick.update(element)
# print(dick)

################################################################################

# # Задание 12:
# def  temperature_farengeit(f):
#     c = 5.0 * (f - 32) / 9
#     print(c)
# temperature_farengeit(10)
#
# def temperature_Celcium(c):
#     f = (9 / 5.0 * c) + 32
#     print(f)
# temperature_Celcium(20)
#
# # Задание 10:
# m_earth = 75
# for_year_moon  = 0
# for i in range(16):
#      for_year_moon = 0.165 *(m_earth + i)
#      print(round(for_year_moon,3),'кг')

## Задание 8:
# import random
#
#
# while True:
#     n1 = int(input('Введите длину числа:'))
#     if n1 < 7:
#         print('слишком короткое число')
#     elif n1 > 31:
#         print('слишком длинное число')
#     else:
#         print(n1)
#         break
#
# while True:
#     n2 = input('Введите цифры из которого состоит либо через пробелы или запятые:')
#     if ' ' in n2 and ',' in n2:
#         print('введите через только запятые или только пробелы')
#     if len(n2) < 5:
#         print ('необходимо ввести больше чисел')
#     elif ',' in n2:
#         print(n2)
#         break
#     elif ' ' in n2:
#         print(n2)
#         break
# lst = str(n2)
# lst.replace(' ,', '')
#
# lst1 = []
# for x in range(n1):
#     x = random.choice(lst)
#     lst1.append(x)
# print(lst1)cd



# # telebot
# #
# from bs4 import BeautifulSoup
# import requests
# import json
#
# JSON = 'kloop.json'
# URL = 'https://kloop.kg/news/'
# HEADERS = {
# 'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
#     }
#
# def get_content():
#     r = requests.get(url=URL, headers=HEADERS, verify=False)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     items = soup.findAll('article', class_='elementor-post')
#
#     new_posts = []
#
#     for item in items:
#         new_posts.append(dict(title=item.find('div', class_='elementor-post__text').find(
#             'h3').find('a').get_text(strip=True), data=item.find('div', class_='elementor-post__meta-data').find(
#             'span', 'elementor-post-date').get_text(strip=True),
#                               photo=item.find('a', 'elementor-post__thumbnail__link').find(
#                                   'div', 'elementor-post__thumbnail').find('img').get('src'),
#                               link=item.find('div', class_="elementor-post__text", href='href').find('h3','a','href')))
#
#     with open('news.json', 'w') as file:
#         json.dump(new_posts, file, indent=4, ensure_ascii=False)
#
#
# def main():
#     get_content()

#
# if name == "main":
#     main()




