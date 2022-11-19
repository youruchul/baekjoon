import sys

total = int(input())
count = int(input())
sum = 0

for i in range(count):
    a,b = map(int,sys.stdin.readline().split())
    sum += (a * b)

if total == sum:
    print("Yes")
else:
    print("No")