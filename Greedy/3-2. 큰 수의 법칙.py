
arr = []
result = 0

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result += arr[n-2] * (m//k)
m -= m//k
result += arr[n-1] * m

print(result)