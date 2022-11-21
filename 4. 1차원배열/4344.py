import sys
C = int(sys.stdin.readline())
for i in range(C):
    testList = list(map(int,sys.stdin.readline().split()))
    c = testList[0]
    scores = testList[1:]
    
    scoreSum = sum(scores)
    avg = scoreSum/c
    avgup = 0

    for i in scores:
        if i > avg:
            avgup += 1
    
    print("{:.3f}%".format(avgup/c*100))

    # if stuavg % 1 == 0:
    #     print("{}00%".format(stuavg))
    # elif stuavg % 0.1 == 0:
    #     print("{}0%".format(stuavg))
    # else:
    #     print("{}%".format(stuavg))