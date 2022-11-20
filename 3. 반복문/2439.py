import sys
n = int(sys.stdin.readline())
c = 1

while c <= n:
    print(('*' * c).rjust(n))
    c += 1