import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sum = 0
cnt = 0

for x in arr:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)