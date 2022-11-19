# Case #1: 2
import sys
count = int(input())

for i in range(1,count+1):
    a,b = map(int,sys.stdin.readline().split())
    #print(type(i))
    print('Case #{}: {}'.format(i,(a+b)))