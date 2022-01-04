# 활동선택 재귀
data = [(1,4), (3,5), (1,6), (5,7), (3,8), (5,9), (6,10), (8,11), (2,13), (12,14)]

n = len(data) # 회의 개수

cnt = 1

def dfs(now):
    # 이번에 now라는 회의를 고른 상황
    min_idx = -1
    for i in range(now + 1, n):
        if data[now][1] <= data[i][0]:
            min_idx = i
            break
    next = min_idx

    if next == -1: return # 기저조건
    global cnt
    cnt += 1 # next라는 회의를 고를 것이니 그 회의를 골랐다고 기록
    dfs(next)
    # next라는 회의를 골라서 진행

dfs(0)
print(cnt)


'''

이렇게도 풀 수 있구나 정도 알기
원래 반복문으로 푼다


개구리 점프
버스 노선
공주 머시기




'''