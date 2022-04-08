import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(9)]
check_1 = True
check_2 = True
for i in range(9):
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(9):
        if a[i][j] in check_list:
            check_list.remove(a[i][j])

    if len(check_list) != 0:
        check_1 = False
        break

for k in range(9):
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for l in range(9):
        if a[l][k] in check_list:
            check_list.remove(a[l][k])

    if len(check_list) != 0:
        check_2 = False
        break

for m in range(9)

if check_1 and check_2:
    print('YES')
else:
    print('NO')