import sys

n = int(sys.stdin.readline())
for i in range(n):
    nn,s = map(str,sys.stdin.readline().split())
    nn = int(nn)
    for j in s:
        print((nn*j),end='')
    print()