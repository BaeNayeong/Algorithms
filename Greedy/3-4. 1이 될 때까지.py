import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k != 0:
        count += n % k
        n = n - n % k
    n = n/k
    count = count+1


print(count)