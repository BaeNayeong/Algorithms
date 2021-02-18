def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []
result = 0
last = 0


for i in range(n+1):
    parent[i] = i


for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(m):
    cost, a, b = edges[i]

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)
