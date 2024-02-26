with open("space.txt", encoding="utf-8") as file:
    data = list(file)

for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

name = input()
while name != "stop":
    done = 0
    for i in data:
        if i[0] == name:
            print(f"Корабль {i[0]} был отправлен с планеты: {i[1]} и его направление движения было: {i[-1]}")
            done += 1
            break
    if done == 0:
        print("error.. er.. ror..")
    name = input()