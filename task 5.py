with open("space.txt", encoding="utf-8") as file:
    data = list(file)

for i in range(len(data)):
    data[i] = data[i].split("*")
    if i + 1 != len(data):
        data[i][-1] = data[i][-1][:-1]

hash = dict()
counter = 1
for i in range(1, len(data)):
    hash[data[i][1]] = data[i][0]
    if counter <= 10:
        print("{" + data[i][1] + "}: {" + hash[data[i][1]] + "}")
        counter += 1
