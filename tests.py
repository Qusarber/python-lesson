#----------------------------------------------------------------------------------------
# 1. написати програму, яка буде знаходити всі числа кратні 7 але не кратні 5, не менше 1000 і не більше 3100.
# Результат вивести через кому в один рядом.
def numbers():
	lst=[]
	for i in range(1000,3101,1):
		if i % 7 == 0 and i % 5 != 0:
			lst.append(i)
	m = map(str, lst)
	k = ', '.join(m)
	return k
print (numbers())


#----------------------------------------------------------------------------------------
#2. написати те ж що в №1, але в 1 рядок( без використання eval )
print(','.join(map(str, [i for i in range(1000,3101) if i % 7 == 0 and i % 5 != 0])))


#----------------------------------------------------------------------------------------
#3. написати функцію, яка буде знаходити факторіал числа.
print('Введіть число, факторіал якого необхідно знайти: ')
n=int(input())
def factorial(n):
	fact = 1
	for i in range(2, n + 1):
		fact *= i
	return fact
print('Результат:',factorial(n))


#----------------------------------------------------------------------------------------
#4. те ж саме, але без рекурсії ( з рекурсією, якщо зробили без рекурсії ).
#рекурсивною функцією знайти факторіал числа 105. 
def factorial(n):
	if n < 2:
		return 1
	else:
		return n * factorial(n-1)
print(factorial(105))


#----------------------------------------------------------------------------------------
#5. написати функцію, яка при заданому n буде генерувати dict вигляду {i: i^2, ...}, де і від 1 до n.
print('Введіть n:')
n = int(input())
def dict_generator (n):
	rezult_dict = {}
	rezult_list = []
	for i in range(1,n+1):
		rezult_dict[i] = i**2
	return rezult_dict
print("Результат:", dict_generator(n))
# Розглядав ще такий варіант виводу, тоді вивід вихлдить ніби в один рядок
# print("вивід варіант №2")
# for k, i in rezult_dict.items():
# 	print(f'{k}:{i}', end=" ")


#----------------------------------------------------------------------------------------
#6. написати те ж що в №5, але генерація в 1 рядок
print('Введіть n:')
n = int(input())
def line_generator (n):
	k = 1
	for i in range(1,n+1):
		i = i**2
		print('{} : {},'.format(k,i), end=' ')
		k += 1
print(line_generator(n))


#----------------------------------------------------------------------------------------
# 7. написати функцію, яка отримує аргумент типу string з числами через кому
# (можливі пробіли(space)), а на виході видає tuple цих чисел
def tuple_from_list():
	print('Введіть стрічку для обробки:')
	input_str = str(input())
	new_str = input_str.replace(" ", "") 	#прибираємо можливі пробіли
	new_tuple = tuple(new_str.split(","))   #розділяємо і заносимо
	return new_tuple
print('Наш tuple: ',tuple_from_list())


#----------------------------------------------------------------------------------------
# 8. написати функцію, яка приймає string зі словами через кому,
# а повертає список із словами відсортованими в алфавітному порядку 
def alphabet_sort():
	print('Введіть стрічку для обробки:')
	input_str = str(input())
	rezult_list = list(input_str.split(','))
	rezult_list.sort()
	return rezult_list
print('Результат:', alphabet_sort())


#----------------------------------------------------------------------------------------
# 9. написати функцію, яка приймає список текстових рядків (list[str]) і
# виводить кожен рядок, роблячи кожну першу букву слова великою
input_lst = ['Aba ab ba ma', 'Ka ta ta', 'Ha rata']
def upper_every_words(input_lst):
	rezult_lst = []
	for i in input_lst:
		i = i.title()
		rezult_lst.append(i)
	return rezult_lst
print(upper_every_words(input_lst))


#----------------------------------------------------------------------------------------
# 10. написати функцію, яка приймає string зі словами, розділеними
# пробілами (одним чи більше) і повертає список із унікальними словами
print("Введіть стрічку для обробки:")
input_str = str(input())
input_lst = input_str.split()
def unikalni_znachenya():
	rezult_list = []
	for i in input_lst:
		if i not in rezult_list:
			rezult_list.append(i)
	return rezult_list
print('Унікальні значення: 'unikalni_znachenya())


#----------------------------------------------------------------------------------------
# 11. написати програму, яка приймає string із бінарними числами,
# розділеними комою, і повертає тільки ті, які діляться на 5 
def binary_division_on_5(lst1):
	rezult_list = []
	for i in lst1:
		if int(i,2) % 5 == 0:
			rezult_list.append(i)
	return rezult_list
assert binary_division_on_5(['1000001','101','100']) == ['1000001', '101']


#----------------------------------------------------------------------------------------
# 12. написати функцію, яка обчислює a+aa+aaa+aaaa при заданому а.
# приклад, а=1 -- 1+11+111+1111
def suma(a,n): #зробив з можливістю міняти кількість "перетворень"
	a=str(a)
	sum = 0 
	for i in range(1,n+1):
		sum = sum + int(str(a*i))
	return sum
assert suma(3,4) == 3702
assert suma(5,4) == 6170


#----------------------------------------------------------------------------------------
# 13. написати функцію, яка перевіряє пароль на відповідність правилам:
#     1. At least 1 letter between [a-z]
#     2. At least 1 number between [0-9]
#     1. At least 1 letter between [A-Z]
#     3. At least 1 character from [$#@]
#     4. Minimum length of transaction password: 6
#     5. Maximum length of transaction password: 12

import re

def password_chek():
	while True:
		password = input("Введіть пароль: ")
		if len(password) < 6 or len(password) > 12:
			print('Упевніться, що ваш пароль має від 6 до 12 символів')
		elif re.search('[0-9]',password) is None:
			print('Упевніться, що ваш пароль має хоча б одну цифру')
		elif re.search('[A-Z]',password) is None: 
			print('Упевніться, що ваш пароль має хоча б одну велику букву')
		elif re.search('[a-z]',password) is None: 
			print('Упевніться, що ваш пароль має хоча б одну малу букву')
		elif re.search('[$,#,@]',password) is None: 
			print('Упевніться, що ваш пароль має хоча б один символ із $,#,@')
		else:
			print('Ваш пароль відповідає правилам')
			break

password_chek()


#----------------------------------------------------------------------------------------
# 14. написати функцію, яка буде сортувати tuple із 3х значень. tuple вигляду (імя, вік, та рейтийнг).
# Пріорітет сортування - по імені, потім по віку, потім по рейтингу.
rating = [('Anton',23,101),('Max',18,100),('Max',19,100),('Anton',22,90)]
from operator import itemgetter

def sort(rating):
    return sorted(sorted(sorted(rating, key=itemgetter(2)),key=itemgetter(1)),key=itemgetter(0))

print('Результат сортування', sort(rating))


#----------------------------------------------------------------------------------------
# 15. На вході функція отримує список strings із переміщеннями робота вигляду "1 UP", "2 LEFT", "3 DOWN", і т.д.
# робот може рухатись тільки в 4 сторони(UP,DOWN,LEFT,RIGHT).
# функція повинна повертати відстань між початковою і кінцевою точками робота.
lst = ['1 UP','2 LEFT','3 DOWN']
def mooves (lst):
	x_end = 0
	y_end = 0	
	for i in range(len(lst)):
		input_lst = list(lst[i].split())
		if str(input_lst[1]) == "UP":
			y_end = y_end + int(input_lst[0])
		if str(input_lst[1]) == "DOWN":
			y_end = y_end - int(input_lst[0])
		if str(input_lst[1]) == "LEFT":
			x_end = x_end - int(input_lst[0])
		if str(input_lst[1]) == "RIGHT":
			x_end = x_end + int(input_lst[0])
				
	distance = (x_end*x_end + y_end*y_end)**(0.5)
	return(distance)

print("Відстань", mooves(lst))	


#----------------------------------------------------------------------------------------
# 16. Написати функцію, яка буде рахувати частоту використання слів у тексті.
# Функція повинна роздрукувати слова і частоту в алфавітному порядку.
def words_frequency():
	print('Введіть текст для обробки:')
	input_str = str(input())
	edited_str = input_str.replace(",", "")
	edited_str = edited_str.replace(".", "")
	input_lst = edited_str.split()
	frequency = {}
	for word in input_lst:
		count = frequency.get(word,0)
		frequency[word] = count + 1
	frequency_list = frequency.keys()

	print("Частота повторень:")
	for words in frequency_list:
		print(words, frequency[words])
words_frequency