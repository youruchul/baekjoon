import sys

n = int(sys.stdin.readline())
a = str(sys.stdin.readline().strip())
sum = 0
for i in a:
    sum += int(i)
print(sum)