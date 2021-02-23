num = input() # String 형으로 입력
result = int(num[0]) # 결과값을 저장할 변수에 첫번째 값 넣어줌

for i in range(1, len(num)): # 결과값의 끝까지 모두 검사
    if result == 0 or num[i] == 0: 
        # result가 0이거나 현재 검사하는 값이 0인 경우 곱해주면 0이 되기 때문에 해당 경우는 더해줌
        result += int(num[i])
    else: 
        # 0이 아닌 경우에는 곱해주는 경우가 값이 더 커지기 때문에 곱해줌
        result *= int(num[i])

print(result)