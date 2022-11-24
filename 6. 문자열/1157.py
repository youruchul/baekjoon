import sys
s = sys.stdin.readline().strip()

s = s.lower()
alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}

for i in s:
    alpha[i] += 1
num,count,maxnum = 0,0,0
for i in alpha:
    if num > alpha[i]:
        pass
    elif num == alpha[i]:
        if num == 0:
            pass
        else:
            count += 1
    else:
        num = alpha[i]
        count = 0
        target = i

if count == 0:
    maxnum = target.upper()
else:
    maxnum = '?'

print(maxnum)
