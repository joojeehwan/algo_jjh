


n = int(input())

#1차원 리스트 입력받기
fears = list(map(int, input().split()))

#오름차순 정렬 => 가장 작은게 앞으로 오는,,!
fears.sort()

#총 그룹의 수
result = 0

#그룹에 포함된 모험가의 수
count = 0

for fear in fears: #공포도가 낮은 것 부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기! 일단 넣기
    if count >= fear:# 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성! 왜냐면 공포도를 넘어서니깐!
        result += 1 #총 그룹의 수 증가 시키기
        count = 0 #현제 그룹에 포함된 모험가의 수 초기화

print(result) # 결과 출력



