"""Файл для решения задачи 4 предпроф экзамена.
Программа позволяет создать хэш-таблицу для кораблей и
выводит первые десять из них в необходимом по заданию виде"""

# Открытие файла с данными
with open("space.txt", encoding="utf-8") as file:
    data = list(file)

# Приведение данных в необходимый для работы программы вид
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

# Создание хэш-таблицы по условию задачи
hash = dict()
counter = 1
for i in range(1, len(data)):
    hash[data[i][1]] = data[i][0]
    if counter <= 10:
        print("{" + data[i][1] + "}: {" + hash[data[i][1]] + "}")
        counter += 1
