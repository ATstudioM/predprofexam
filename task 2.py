"""Файл для решения задачи 2 предпроф экзамена.
Программа позволяет отсортировать корабли по их номерам и
вывести первые 10 кораблей при сортировке по возрастанию"""

# Открытие файла с данными
with open("space.txt", encoding="utf-8") as file:
    data = list(file)

# Приведение данных в необходимый для работы программы вид
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]
    if i > 0:
        data[i][0] = data[i][0].split("-")

# Сортировка всех данных в списке data по возрастанию по номеру корабля с помощью сортировки пузырьком
headline = data.pop(0)
print(data[0][0][1])
for i in range(len(data)):
    for j in range(len(data) - 1):
        if int(data[j][0][1]) > int(data[j + 1][0][1]):
            data[j], data[j + 1] = data[j + 1], data[j]

# Вывод необходимых кораблей
for i in range(10):
    print(data[i][0][0] + "-" + data[i][0][1])
