import sys

a,b = sys.stdin.readline().split()

a = a[2]+a[1]+a[0]
b = b[2]+b[1]+b[0]

a,b = str(a),str(b)
if a >= b:
    print(a)
else:
    print(b)