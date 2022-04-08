# import sys

# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# ave = int(sum(arr)/n + 0.5)
# min = float('inf')

# for idx, i in enumerate(arr):
#     tmp = abs(i - ave)

#     if tmp < min:
#         min = tmp
#         score = i
#         res = idx + 1
#     elif tmp == min:
#         if i > score:
#             score = i
#             res = idx + 1

# print(ave, res)

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ave = int(sum(arr)/n + 0.5)
min = float('inf')
res = 0

for idx, x in enumerate(arr):
    dif = abs(x - ave)

    if dif < min:
        min = dif
        score = x
        res = idx + 1
    elif dif == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)