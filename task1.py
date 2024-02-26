"""Файл для решения задачи 1 предпроф экзамена.
Программа сначала заменяет все нулевые значениня координат в таблице,
а затем выводит корабли с координатами в формате “ <ShipName> - (<x>, <y>)”"""

# Открытие файла с данными
with open("space.txt", encoding="utf-8") as file:
    data = list(file)

# Приведение данных в необходимый для работы программы вид
for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

# Подготовка списка для вывода кораблей с их координатами
to_print = []
# Поиск и замена всех нулевых значений координат в соответствии с условием задачи
for i in range(len(data)):
    name = data[i][0].split('-')
    if data[i][2] == "0 0":
        direction = data[i][-1].split()
        if int(name[1][0]) > 5:
            x = int(name[1][0]) + int(direction[0])
        else:
            x = (int(name[1][0]) + int(direction[0])) * 4 + len(data[i][1])
        if int(name[1][1]) > 3:
            y = int(name[1][1]) + len(data[i][1]) + int(direction[1])
        else:
            y = -1 * (int(name[1][0]) + int(direction[1])) * int(name[1][1])
        data[i][2] = f"{x} {y}"
    # Добавление данных о корабле в список, если в их имени последняя буква V
    if name[0][-1] == "V":
        to_print.append(data[i])

# Запись данных в новый txt файл
file = open("space_new.txt", "w", encoding="utf-8")
for i in range(len(data)):
    to_add = ""
    for j in range(4):
        to_add += data[i][j]
        if j < 3:
            to_add += "*"
        elif i + 1 != len(data):
            to_add += "\n"
    file.writelines(to_add)
file.close()

# Вывод всех кораблей, у которых последняя буква в имени V
for i in to_print:
    coordinates = i[2].split()
    print(f"{i[0]} - ({coordinates[0]}, {coordinates[1]})")
