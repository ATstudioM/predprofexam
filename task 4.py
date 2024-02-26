from csv import writer


def generate_password(info):
    """
    Функция для генерации паролей для каждого из кораблей
    :param info:
    Список со всеми данными о корабле
    :return:
    Строка с паролем, в соотвествии с условием задачи
    """
    password = info[1][-3:]
    password = password + info[0][2] + info[0][1]
    password = password + info[1][2] + info[1][1] + info[1][0]
    password = password.upper()
    return password


with open("space.txt", encoding="utf-8") as file:
    data = list(file)

for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

data[0].append("password")
for i in range(1, len(data)):
    data[i].append(generate_password(data[i]))

file = open("space_uniq_password.csv", 'w', encoding="utf-8")
writing = writer(file, delimiter=";")
writing.writerows(data)
file.close()
