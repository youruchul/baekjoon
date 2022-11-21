import sys

list = []
noList = []
for i in range(28):
    list.append(int(sys.stdin.readline()))

for j in range(1,31):
    if j in list:
        pass
    else:
        noList.append(j)

noList.sort()
print(noList[0])
print(noList[1])