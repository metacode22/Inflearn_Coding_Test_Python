# import sys
# input = sys.stdin.readline

# t = int(input())

# for i in range(t):
#     s = input().rstrip().upper()
#     size = len(s)

#     for j in range(size//2):
#         if s[j] != s[-j - 1]:
#             print(f'#{i + 1} NO')

#         else:
#             print(f'#{i + 1} YES')

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input().rstrip().upper()
    if s == s[::-1]:
        print(f'#{i + 1} YES')

    else:
        print(f'#{i + 1} NO')