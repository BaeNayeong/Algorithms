from collections import deque

v, e = map(int, input().split())  # 노드의 개수, 간선의 개수
indegree = [0] * (v + 1)  # 모든 노드에 대한 진입차수 0으로 초기화
graph = [[] for i in range(v + 1)]  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
