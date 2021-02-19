n = int(input())
edges = list(map(int, input().split()))
nodes = list(map(int, input().split()))


min = nodes[0]
length = edges[0]
result = nodes[0] * edges[0]


for i in range(1, n-1):
    length = edges[i]

    if min > nodes[i]:
        min = nodes[i]

    result += min * length


print(result)
