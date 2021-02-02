import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
times = 0

for i in range(1, n+1):
    if graph[c][i] != INF and graph[c][i] != 0:
        count += 1
        if graph[c][i] > times:
            times = graph[c][i]

print(count)
print(times)
