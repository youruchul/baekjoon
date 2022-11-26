import sys

a,b,c = map(int,sys.stdin.readline().split())
bep = 0 

if c>b:
    bep = (a / (c-b)) + 1
    print(int(bep))
else:
    print(-1)