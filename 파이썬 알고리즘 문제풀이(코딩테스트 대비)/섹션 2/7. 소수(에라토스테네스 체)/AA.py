from re import L
import sys, math

def reverse(x):
    res = 0

    while x > 0:
        tmp = x % 10
        res = res*10 + tmp
        x = x //10

    return res

def is_prime(x):
    if x <= 1:
        return False

    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False

    return True

n = int(sys.stdin.readline())
arr = list(map(int ,sys.stdin.readline().split()))

for x in arr:
    tmp = reverse(x)

    if is_prime(tmp):
        print(tmp, end='')
