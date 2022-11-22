import sys

n = int(sys.stdin.readline())
hansu = []
if n < 100:
    for k in range(n):
        hansu.append(k)
    print(len(hansu))
else:
    for i in range(100,n+1):
        Fnum = str(i)[0]
        Bnum,cha,count = 0,0,0        
        chaset = set()
        for j in range(len(str(i))):
            count += 1
            if count == 1:
                continue
            Bnum = str(i)[j]
            cha = int(Fnum) - int(Bnum)
            chaset.add(cha)
            Fnum = Bnum
        if len(chaset) == 1:
            hansu.append(i)
    print(len(hansu)+99)