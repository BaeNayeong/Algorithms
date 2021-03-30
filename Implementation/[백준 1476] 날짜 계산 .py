e, s, m = map(int, input().split())
x = 0
y = 0
z = 0
result = 0

while True:
    x += 1
    y += 1
    z += 1
    result += 1

    if x==16: x = 1
    if y==29: y = 1
    if z==20: z = 1

    if x==e and y==s and z==m:
        break

print(result)
