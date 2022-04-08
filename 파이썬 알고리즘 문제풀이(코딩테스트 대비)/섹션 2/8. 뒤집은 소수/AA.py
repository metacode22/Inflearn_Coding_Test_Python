import sys, math

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def reverse(x):
    res = 0

    while x > 0:
        tmp = x % 10
        res = res * 10 + tmp
        x = x // 10
    return res

def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

for j in arr:
    j_reversed = reverse(j)

    if is_prime(j_reversed):
        print(j_reversed, end=' ')