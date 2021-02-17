n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

print()
for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0: # 팀 합치기 연산
        union_parent(parent, a, b)
    elif op == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print('YES')
        else:
            print('NO')
