import sys
AA = [sys.stdin.readline().strip() for _ in range(2)]
A = AA[0]
B = AA[1]
BB = []
for i in B:
    BB.append(i)

a,b,c = BB[0],BB[1],BB[2]

print(int(A)*int(c))
print(int(A)*int(b))
print(int(A)*int(a))
print(int(A)*int(B))