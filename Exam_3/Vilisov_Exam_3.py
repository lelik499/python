#1 Создайте класс "Студент", который имеет атрибуты имя и возраст, а также методы "изменить_имя" и "изменить_возраст". Напишите функцию,
# которая создает объект класса "Студент", запрашивая у пользователя его имя и возраст, а затем предлагает пользователю изменить имя и возраст.

# class Student:
# 	name=''
# 	age=''
# 	def change_name(self,name):
# 		 self.name = name
# 	def change_age(self,age):
# 		self.age = age
#
# def new_change():
#     s = Student()
#     s.name=input('Введите ваше имя')
#     s.age=input('Введите возраст')
#     s.change_name=(input('Введите новое имя'))
#     s.change_age=(input('Введите возраст'))
#
# new_change()
#

# 2 Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов всех четных чисел в списке.
# spisok=[1,2,3,4,5,6,7]
# def fun(spisok):Не желаете ли вы изменить свое имя и возраст?
#     n=0
#     for i in spisok:
#         if i %2==0:
#              n+=i**2
#     return n
# print(fun(spisok))

# 3 Создайте класс "Калькулятор", который имеет атрибуты "значение" и методы "сложить", "вычесть", "умножить" и "разделить". Напишите функцию, которая
# создает объект класса "Калькулятор" и позволяет пользователю выполнить несколько арифметических операций с его помощью.
# class Calc:
#
#     def __init__(self):
#         self.a = float(input('Введите число'))
#         self.b = float(input('Введите число'))
#     def add(self): return self.a + self.b
#     def differ(self): return self.a - self.b
#     def mul(self): return self.a * self.b
#     def div(self): return self.a / self.b
# while True:
#     dist = input('Выберите  операцию: ')
#     if dist not in '+-/*' or dist=='': break
#     my_calc = Calc()
#     if dist == '+': print(my_calc.add())
#     elif dist == '-': print(my_calc.differ())
#     elif dist == '*': print(my_calc.mul())
#     elif dist == '/': print(my_calc.div())
#     else:
#         print('Такой операции нет')
#         break

# 4Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска", "цвет" и метод "описание",
# который выводит описание автомобиля в виде строки. Напишите функцию, которая создает объект класса "Автомобиль", запрашивая у пользователя информацию
# о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.

# class Car:
#     make = ''
#     model = ''
#     year = ''
#     color = ''
#
#     def get_info(self):
#         return f'Автомобиль {self.make}, модель{self.model},год выпуска {self.year},цвет {self.color}'
#
#
# def my_fun():
#     a = Car()
#     a.make = input('Введите марку автомобиля ')
#     a.model = input('Введите модель ')
#     a.year = input('Введите год выпуска')
#     a.color = input('Введите цвет ')
#     print(a.get_info())
#
# my_fun()


# 5Создайте класс "Сотрудник", который имеет атрибуты "имя", "фамилия", "должность" и метод "описание",
# который выводит описание сотрудника в виде строки. Создайте класс "Отдел", который имеет атрибуты "название" и "список_сотрудников",
# а также методы "добавить_сотрудника" и "удалить_сотрудника". Напишите функцию, которая создает объект класса "Отдел", запрашивая
# у пользователя его название, а затем предлагает пользователю добавить несколько сотрудников в отдел, после чего выводит список всех сотрудников
# в отделе и их описания. Затем функция предлагает пользователю удалить одного из сотрудников и выводит обновленный список сотрудников и их описания.


# class sotrudnik:
#     name = 'USERNAME'
#     age = None
#     dol = None
#     def opisanie(self):
#         print(f'Имя: {self.name}, возраст: {self.age}, должность: {self.dol}')
# class department:
#     department_name = None
#     sotr_list = []
#     def sotr_add(self, name_s):
#         self.sotr_list.append(name_s)
#     def sotr_del(self, name_s):
#         self.sotr_list.remove(name_s)
#
# def create_sotr(dep_name):
#     dep_object = department()
#     dep_object.department_name = dep_name
#     a = input('Хотите ли добавить сотрудника? ')
#     if a: dep_object.sotr_add(input('Введите имя: '))
#     print(dep_object.sotr_list)
#     b = input('Хотите ли удалить сотрудников?')
#     if b: dep_object.sotr_del(input('Введите имя: '))
#     print(dep_object.sotr_list)
#
# create_sotr('Overone')
#
