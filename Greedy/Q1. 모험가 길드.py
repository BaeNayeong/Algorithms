n = int(input()) # 모험가의 수 입력
arr = list(map(int, input().split())) # 모험가 공포도 입력
count = 0 # 그룹의 수 저장
index = 0

arr.sort(reverse=True) # 모험가의 공포도를 내림차순으로 정렬

while index < n: # 공포도가 제일 큰 모험가부터 검사
    count = count + 1 # 그룹에 포함
    index = index + arr[index] # 공포도가 높은 모험가에 포함된 그룹 다음부터 시작
    # 공포도가 가장 큰 모험가는 해당 공포도만큼의 사람을 데리고 있어야 하기 때문에 해당 방식으로 알고리즘을 접근했다
print(count)