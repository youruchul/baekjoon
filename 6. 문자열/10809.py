import sys
a = str(sys.stdin.readline().strip())

alpha = "abcdefghijklmnopqrstuvwxyz"

for al in alpha:
    if al in a:
        print(a.find(al),end=' ')
    else:
        print(-1,end=' ')