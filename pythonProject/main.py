# 1. Есть список состоящий из слов и чисел,
# нужно записать в файл построчно сначала
# слова в порядке их длины, а после слов числа в порядке возрастания.
#
# 2. Добавьте на свой РАБОЧИЙ СТОЛ папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
# Создаем именно на РАБОЧЕМ СТОЛE

with open('/D:/Programming/Projects/python/pythonProject/example.txt/main.py', 'r', encoding='utf8') as f:
    l = f.readlines() #вытаскиваем все строки
print(l)
 print('\nflkjjdf\n'.strip()) #strip удаляет пробелы и переносы по бокам
chisla = [] #здесь будут слова
slova = [] #здесь будут числа
for i in l:
    i = i.strip()
    if i.isdigit(): chisla.append(int(i))
    else: slova.append(i)
print(chisla, slova)

chisla.sort()
slova.sort(key=len)

print(chisla+slova)