inFile = open('input.txt', 'r', encoding='utf8')
result9 = []
result10 = []
result11 = []
myList = (inFile.readline()).split()
while myList != []:
    if myList[2] == "9":
        result9.append(int(myList[3]))
    elif myList[2] == "10":
        result10.append(int(myList[3]))
    elif myList[2] == "11":
        result11.append(int(myList[3]))
    myList = (inFile.readline()).split()
a, b, c = -1, -1, -1
s, t, w = 0, 0, 0
for i in range(len(result9)):
    if result9[i] > a:
        s = 1
        a = result9[i]
    elif result9[i] == a:
        s += 1
for j in range(len(result10)):
    if result10[j] > b:
        t = 1
        b = result10[j]
    elif result10[j] == b:
        t += 1
for k in range(len(result11)):
    if result11[k] > c:
        w = 1
        c = result11[k]
    elif result11[k] == c:
        w += 1
print(s, t, w)
list = (a, b, c)
p

