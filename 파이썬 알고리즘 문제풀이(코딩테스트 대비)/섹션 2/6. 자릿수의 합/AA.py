import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def digit_num(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000
for i in arr:
    tot = digit_num(i)

    if tot > max:
        max = tot
        res = i

print(res)