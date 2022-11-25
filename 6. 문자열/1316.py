import sys

n = int(sys.stdin.readline())
groupnum,diff = 0,0

for i in range(n):
    l = []
    a = sys.stdin.readline().strip()
    out = 0
    for aa in a:
        if aa in l:
            if l[len(l)-1] == aa:
                pass
            else:
                out += 1    
        else:
            l.append(aa)
    if out == 0:
        groupnum += 1
    else:
        pass

print(groupnum)