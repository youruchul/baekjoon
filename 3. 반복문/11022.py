'''
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
'''
import sys
count = int(input())

for i in range(1,count+1):
    a,b = map(int,sys.stdin.readline().split())
    #print(type(i))
    print('Case #{}: {} + {} = {}'.format(i,a,b,(a+b)))