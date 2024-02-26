with open("space.txt", encoding="utf-8") as file:
    data = list(file)

for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

to_print = []
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
    if name[0][-1] == "V":
        to_print.append(data[i])

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

for i in to_print:
    coordinates = i[2].split()
    print(f"{i[0]} - ({coordinates[0]}, {coordinates[1]})")
