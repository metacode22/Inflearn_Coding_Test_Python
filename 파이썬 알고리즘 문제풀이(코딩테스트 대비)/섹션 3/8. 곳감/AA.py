import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0, 0, 0, 0, 0])
a.append([0, 0, 0, 0, 0])

for i in a:
    i.insert(0, 0)
    i.append(0)

cnt = 0
for j in range(1, n + 1):
    for k in range(1, n + 1):
        if max(a[j][k], a[j][k - 1], a[j][k + 1], a[j - 1][k], a[j + 1][k]) == a[j][k]:
            cnt += 1

print(cnt)