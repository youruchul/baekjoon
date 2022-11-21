import sys

list = []
for i in range(9):
    list.append(int(sys.stdin.readline()))

limax = max(list)
fimax = list.index(limax)

print(limax)
print(fimax + 1)