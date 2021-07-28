#------------------------------------------------------------------------------------------
#Тема 2. Создание классов и обьектов
import random

class Warrior:

    def health(self, health_amount):
        self.health_amount = health_amount

    def str(self):
        return 'Количество здоровья юнита:({})'.format(self.health_amount)

    def kick(enemy):
        enemy.health_amount -= 20

unit1 = Warrior()
unit2 = Warrior()
unit1.health(100)
unit2.health(100)

while unit1.health_amount and unit2.health_amount > 0:
    attacking_unit =  random.choice(['unit1', 'unit2'])
    if attacking_unit == 'unit1':
        Warrior.kick(unit2)
        print('\n Атаковал unit1, у противника осталось здоровья: {}'.format(unit2.health_amount))
    elif attacking_unit == 'unit2':
        Warrior.kick(unit1)
        print('\n Атаковал unit2, у противника осталось здоровья: {}'.format(unit1.health_amount))
else:
    if unit1.health_amount > 0:
        print('\n Unit1 win')
    elif unit2.health_amount > 0:
        print('\n Unit2 win')




#----------------------------------------------------------------------------------------
#Тема 3. Наследование

class Person:

    def __init__(self, name, surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __str__(self):
        return " Имя сотрудника: {}\n Фамилия сотрудника: {}\n Квалификация сотрудника: {}".format(self.name, self.surname, self.qualification)

    def delete(self):
        print("До свидания мистер {} {}".format(self.name, self.surname))

employee1 = Person('Carl', 'Johnson', 39)
employee2 = Person('Big', 'Smoke', 2)
employee3 = Person('Cesar', 'Vialpando', 21)

min = employee1.qualification
looser = employee1
for employee in [employee1, employee2, employee3]:
    if employee.qualification < min:
        min = employee.qualification
        looser = employee

print("Самое слабое звено мистер {} {} с квалификацией ({})".format(looser.name, looser.surname, looser.qualification))
looser.delete()
input()



#----------------------------------------------------------------------------------------
#Тема 4. Наследование

import random

class Variors:
    id = 1
    def __init__(self):
        self.id = Variors.id
        Variors.id += 1

class Soldiers(Variors):

    def __init__(self):
        Variors.__init__(self)

    def __str__(self):
        return f'{self.id}'

class Heroes(Variors):

    def __init__(self, team):
        Variors.__init__(self)
        self.team = team
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f'Герой {self.id} досяг {self.level} рівня')

    def following_with_hero(self):
        random_follower_id = random.choice(list_team1)
        print(f'Солдат з ID {random_follower_id} прямує за героєм з ID {self.id}')

hero_1 = Heroes('team1')
hero_2 = Heroes('team2')
list_team1 = []
list_team2 = []
for _ in range(50):
    if random.choice(['team1', 'team2']) == 'team1':
        list_team1.append(Soldiers())
    else:
        list_team2.append(Soldiers())

print(f'Солдатів у першого героя - {len(list_team1)}')
print(f'Солдатів у дрогого героя - {len(list_team2)}')
if len(list_team1) > len(list_team2):
    hero_1.level_up()
else:
    hero_2.level_up()

hero_1.following_with_hero()




#---------------------------------------------------------------------------------------
#Тема 5. Полиморфизм 

class ObjectsSum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return ObjectsSum(self.x + other.x, self.y + other.y)
    def __str__(self):
        return '{}, {}'.format(self.x, self.y)


p1 = ObjectsSum(12, 4)
p2 = ObjectsSum(8, 6)
print(p1 + p2)



#---------------------------------------------------------------------------
#Тема 6. Инкапсуляция

class Table:
    def init(self, typ, width, length, height, weight):
        self.typ = typ
        self.__width = width
        self.__length = length
        self.__height = height
        self.__weight = weight
    def get(self, n):
        return getattr(self, f'_Table__{n}')
    def set(self, attr, val):
        setattr(self, f'_Table__{attr}', val)

table = Table()
table.set('typ', 4)
print(table.get('typ'))




#-------------------------------------------------------------------------------
#Тема 7. Композиция

class WinDoor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def squareWinDoor(self):
        return self.x * self.y

class Room:
    def __init__(self, width, lenght, height):
        self.width = width
        self.lenght = lenght
        self.height = height
        self.wd = []
    
    def ollSurface(self):
        return 2 * self.height * (self.width + self.lenght)
   
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
   
    def workSurface(self):
        new_square = self.ollSurface()
        for i in self.wd:
            new_square -= i.squareWinDoor()
        return new_square
   
    def countRoll(self, w = 1, l = 10):
        self.roll_square = w * l
        return self.workSurface() / self.roll_square

print("Введіть ширину кімнати:")
w_room = int(input())
print("Введіть довжину кімнати:")
l_room = int(input())
print("Введіть висоту кімнати:")
h_room = int(input())
r1 = Room(w_room, l_room, h_room)
print("Введіть кількість вікон та дверей разом:")
n = int(input())

for i in range(1, n+1):
    print("Введіть висоту і ширину {} вікна / дверей:".format(i))
    w_win_door,l_win_door = map(int, input().split())
    r1.addWD(w_win_door, l_win_door)

print("Площа робочої поверхні: {}".format(r1.workSurface()))
print("Кількість необхідних рулонів: {}".format(r1.countRoll()))




#-------------------------------------------------------------------------------
#Тема 8. Перегрузка операторов

import math

class Snow:
    def __init__(self, amount):
        self.snow_amount = amount

    def __add__(self, n):
        self.snow_amount += n
        return self.snow_amount

    def __sub__(self, n):
        self.snow_amount -= n
        return self.snow_amount

    def __mul__(self, n):
        snow_amount *= n
        return self.snow_amount

    def __truediv__(self, n):
        self.snow_amount /= n
        return round(self.snow_amount)

    def __call__(self, new_quantity):
        self.quantity_of_snowflakes = new_quantity

    def makeSnow(self, snow_amount_in_a_row):
        string_of_snowfall = ""
        amount_of_rows = int(self.snow_amount) // snow_amount_in_a_row
        for i in range(amount_of_rows):
            string_of_snowfall += ("*" * snow_amount_in_a_row)
            string_of_snowfall += "\n"
        remain_snowflakes = (int(self.snow_amount) - amount_of_rows * snow_amount_in_a_row)
        string_of_snowfall += "*" * remain_snowflakes
        return string_of_snowfall

snow = Snow(4)
snow.__sub__(1)
print(snow.makeSnow(1))