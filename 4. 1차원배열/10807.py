import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
find = int(sys.stdin.readline())

count = nums.count(find)
print(count)