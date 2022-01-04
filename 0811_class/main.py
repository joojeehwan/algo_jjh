


#델타배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]



N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


#1
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            #arr[ni][nj]
            if 0 <= ni < N and 0 <= nj < M: # 범위를 한정 짖는 것!
                arr[ni][nj]




#2
for i in range(N):
    for j in range(M):
        for dr, dc in [[0,1], [1, 0], [0, -1], [-1, 0]]:
            ni = i +dr
            nj = j + dc
            if 0 <= ni < N and 0 <= nj < M:  # 범위를 한정 짖는 것!
                arr[ni][nj]

#arr[i][j]에서 len(arr[i])는 열의 갯수


# 지그재그 순회 ? 가 기억이 안나면 열을 홀짝으로 구분해서!


#지그재그 순회 공식의 경우 i % 2가 짝수면 0이라 단슨히 j만 더해진다!




#부분 집합 자체의 출력