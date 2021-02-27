n = int(input())
arr = list(input().split())

x, y = 1, 1
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
types = ['R', 'L', 'U', 'D']

for a in arr:
    for i in range(0, len(types)):
        if a == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue

            x = nx
            y = ny

print(y, x)