import sys

# sys.stdin = open('input.txt', 'rt')         # rt는 read text
n, k = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    
    if cnt == k:
        print(i)
        break
else:
    print(-1)