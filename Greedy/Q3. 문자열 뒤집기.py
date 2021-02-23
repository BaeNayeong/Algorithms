arr = input()

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

if arr[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        if arr[i] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count1, count0))