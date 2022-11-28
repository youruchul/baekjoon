# https://hongcoding.tistory.com/33
import sys

n = int(sys.stdin.readline())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line % 2 == 0: # 짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("{}/{}".format(top,bottom))
# -----------------------------------------------------
# 2번째 시도 - 시간초과
# import sys
# n = int(sys.stdin.readline())

# sum,way,cnt = 2,0,1

# for i in range(n): # 0 1 2 3 4
#     if sum % 2 == 1:
#         way = 1
#     else:
#         way = 2

#     if way == 1:
#         B = sum - cnt
#         F = sum - B
#     else:
#         F = sum - cnt
#         B = sum - F
#     cnt += 1
#     if sum == cnt:
#         sum += 1
#         cnt = 1

# print('{}/{}'.format(F,B))
# -----------------------------------------------------
# 1번째 시도 - 시간초과
# import sys

# n = int(sys.stdin.readline())
# F,B = 0,0
# comend, baccom = 's',''

# for i in range(n):
#     baccom = comend
#     if comend == 's':
#         B += 1
#         F += 1
#     if comend == 'r':
#         B += 1
#     elif comend == 'ld':
#         F += 1
#         B -= 1
#     elif comend == 'd':
#         F += 1
#     elif comend == 'ru':
#         F -= 1
#         B += 1
    
#     if F == 1 and B == 1:
#         comend = 'r'
#     elif F == 1 and B != 1:
#         if baccom == 'r':
#             comend = 'ld'
#         else:
#             comend = 'r'
#     elif F != 1 and B == 1:
#         if baccom == 'ld':
#             comend = 'd'
#         else:
#             comend = 'ru'
#     else:
#         pass
    
# print('{}/{}'.format(F,B))