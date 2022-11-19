import sys
x = [1, 1, 2, 2, 2, 8]
a,b,c,d,e,f = map(int,sys.stdin.readline().split())
y = [a,b,c,d,e,f]
z = []
num = 0

for i in range(6):
    z.append(x[num]-y[num])
    num += 1


for i in z:
    print(i,end=" ")
