s = input()

result = 1000
cut = 1

while cut < len(s):   # cut 증가시킴
    index = 0
    num = 1
    count = len(s)

    while index < len(s):     # 각 cut마다 문자열에 적용해줌
        compare = s[index:index+cut]
        index += cut

        if compare == s[index:index+cut]:
            num += 1
            index += cut
            count = count - cut

        else:
            if num != 1:
                count += len(str(num))
            num = 1

    if num != 1:
        count += len(str(num))

    result = min(result, count)
    cut += 1

print(result)