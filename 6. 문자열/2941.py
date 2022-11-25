import sys

s = sys.stdin.readline().strip()
sum,back,back2 = 0,0,0

for i in s:
    if back2 == 'd':
        if back == 'z':
            if i == '=':
                sum -= 2
    elif back == 'z':
        if i == '=':
            sum -= 1            
    if back == 'c':
        if i == '=' or i == '-':
            sum -= 1
    elif back == 'd':
        if i == '-':
            sum -= 1
    elif back == 'l':
        if i == 'j':
            sum -= 1
    elif back == 'n':
        if i == 'j':
            sum -= 1
    elif back == 's':
        if i == '=':
            sum -= 1
    
    sum += 1
    back2 = back
    back = i

print(sum)