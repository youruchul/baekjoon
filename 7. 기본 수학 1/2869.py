import sys

A,B,V = map(int,sys.stdin.readline().split())
if A == V:
    day = 1
elif A-B == 1:
    day = (V-A)/(A-B) + 1
elif (V-A)%(A-B) == 0:
    day = (V-A)/(A-B) + 1
else:
    day = (V-A)/(A-B) + 2
print(int(day))

# https://www.acmicpc.net/board/view/88693
# 12 10 102