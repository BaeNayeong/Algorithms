import sys
input = sys.stdin.readline


n, m = map(int, input().split())
result = 0


for _ in range(n):
    row = list(map(int, input().split()))
    if result < min(row):
        result = min(row)


print(result)