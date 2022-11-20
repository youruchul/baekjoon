num = int(input())
a,b,count = 0,0,0
checkNum = num

while True:
    if num < 10:
        a = 0
        b = num
    else:
        a = num//10
        b = num%10
    sum = a + b
    num = (b * 10) + (sum % 10)
    count += 1
    if checkNum == num:
        break

print(count)