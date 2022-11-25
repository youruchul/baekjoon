import sys
l = []
for i in range(9):
    l.append(int(sys.stdin.readline()))
lco = l.copy()
for i in range(9):
    l1 = lco.copy()
    l1[i] = 0
    l2 = l1.copy()
    for j in range(8):
        l2.sort()
        l3 = l2.copy()
        l3[j+1] = 0
        if sum(l3) == 100:
            l3.sort()
            l4 = l3.copy()
            break

for k in l4[2:]:
    print(k)