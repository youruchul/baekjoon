import sys

num = int(sys.stdin.readline())
myList = list(map(int,sys.stdin.readline().split()))
maxList = max(myList)
myList2 = []
for i in myList:
    myList2.append(i/maxList*100)

sum = 0
for i in myList2:
    sum += i
avg = sum / num
print(avg)