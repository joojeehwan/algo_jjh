'''


토마토 7576 복습하면서,,!

bfs 다시 정리,,!




'''


import sys

from collections import deque


M, N = map(int ,sys.stdin.readline().slplit())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#1. 그래프 구성


#2. queue 생성

q = deque()



#3. 시작점 세팅

for row in range(N):
    for col in range(M):
        if MAP[row][col] == 1:
            q.append([row, col])

ans = -1

#.7 4 ~ 6 단계 반복! 
while len(q) != 0 :
    
    #4. 큐에 가장 앞에 있는 것 뽑기
    now = q.popleft()
    now_row = now[0]
    now_col = now[1]
    ans = MAP[now_row][now_col] # 맵 자체를 비지트 배열로 사용!

    #5. next를 찾기!
    
    #상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue

        if MAP[next_row][next_col] != 0 :
            continue

        #6 next를 queue에 추가
        MAP[next_row][next_col] = MAP[now_row][now_col] + 1
        q.append([next_row, next_col])



#세로의 칸수 ?! 밑으로 내려가겠지!
for row in range(N):
    for col in range(M):
        if MAP[row][col] == 0:
            ans = 0

print(ans - 1)



