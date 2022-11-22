def selfnumber():
    selfNumList = []
    for i in range(1,10001):
        i = str(i)
        if len(i) == 1:
            selfNumList.append(int(i)+int(i[0]))
        elif len(i) == 2:
            selfNumList.append(int(i)+int(i[0])+int(i[1]))
        elif len(i) == 3:
            selfNumList.append(int(i)+int(i[0])+int(i[1])+int(i[2]))
        elif len(i) == 4:
            selfNumList.append(int(i)+int(i[0])+int(i[1])+int(i[2])+int(i[3]))
        elif len(i) == 5:
            selfNumList.append(int(i)+int(i[0])+int(i[1])+int(i[2])+int(i[3])+int(i[4]))
    
    for j in range(1,10001):
        if j in selfNumList:
            pass
        else:
            print(j)

selfnumber()