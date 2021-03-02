input_data = input()
x = ord(input_data[0]) - ord('a') + 1
y = ord(input_data[1]) - ord('0')

count = 0
move = [(1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

for i in range(8):
    dx = x + move[i][0]
    dy = y + move[i][1]

    if dx > 8 or dy > 8 or dx < 1 or dy < 1:
        continue

    count += 1

print(count)