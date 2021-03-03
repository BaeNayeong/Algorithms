n, m = map(int, input().split())
a, b, d = map(int, input().split())
move_types = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = [0, 3, 2, 1]
result = 0
array = []

for _ in range(4):
    array.append(list(map(int, input())))

da = 0
db = 0

while True:
    d = (d+1) % 4
    da = a + move_types[d][0]
    db = b + move_types[d][1]

    array[a][b] = 1

    if array[da][db] == 0:
        a = da
        b = db
        result += 1

    if array[a-1][0] == 1 and array[a][b-1] == 1 and array[a+1][b] == 1 and array[a][b+1] == 1 and array[a][b] == 1:
        break

print(result)
