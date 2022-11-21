import sys

n = int(sys.stdin.readline())
score = 0
count = 0
for i in range(n):
    ox = sys.stdin.readline()
    for j in ox:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
    score,count = 0,0