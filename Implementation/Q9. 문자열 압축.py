s = input()

result = 1000
cut = 0

while cut < len(s):   # cut 증가시킴
    index = 0
    num = 0
    count = len(s)

    while index < len(s):     # 각 cut마다 문자열에 적용해줌
        compare = s[index:index+cut]
        index += cut+1

        if compare == s[index:index+cut]:
            num += 1
            index += cut+1
            count = count - cut - 1

            if len(str(num)) != 0:
                count += len(str(num))
        else:
            index += 1

    if result > count:
        result = count

    cut += 1

print(result)