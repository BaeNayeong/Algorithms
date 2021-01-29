import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())

#2차원 리스트 만들기, 모든 값 무한으로 초기화
graph = [[INF] *(n+1) for _ in range(n+1)]

#자기 자신에게서 자기 자신으로 가는 비용 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보 입력받아 그 값으로 초기화
for _ in range(m):
    #a->b 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

#수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b])
    print()