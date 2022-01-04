
import sys
from collections import deque


N, M = map(int,sys.stdin.readline().split())

MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

q = deque()



for row in range(N):
    for col in range(M):
        if MAP[row][col] == 1:
            visited[row][col] = 1
            q.append([row, col])



while q:

    now = q.popleft()
    now_row = now[0]
    now_col = now[1]




    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue

        if MAP[next_row][next_col] != 0:
            continue


#map을 비짓배열로 쓰네,,?
        visited[next_row][next_col] = 1
        q.append([next_row, next_col])


####################################

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
MAP = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# 1. 그래프 구성

# 2. queue생성
q = deque()

# 3. 시작점 세팅
for row in range(N):
    for col in range(M):
        if MAP[row][col] == 1:
            q.append([row, col])

ans = -1
# 7. 4~6단계 반복
while len(q) != 0 :

    now = q.popleft()
    now_row = now[0]
    now_col = now[1]
    ans = MAP[now_row][now_col] #MAP 자체를 비짓배열로 사용!

    # 5. next찾기
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue #맵을 넘어가면 무시
        if MAP[next_row][next_col] != 0:
            continue # 안익은 토마토가 아니면 무시

        #6. next를 queue에 추가
        MAP[next_row][next_col] = MAP[now_row][now_col] + 1
        q.append([next_row, next_col])
# 1가지 팁
# 모든 토마토가 익어가는데 필요한 시간

for row in range(N):
    for col in range(M):
        if MAP[row][col] == 0:
            ans = 0
print(ans - 1)
