'''

BFS로 풀어야 할 것 같은데?!

일단 기본 bfs를 적어보자!


높아지는 순간에만 추가 연료!

'''

from collections import deque
INF = int(1e9)



T = int(input())



for tc in range(1, T+1):

    N = int(input())

    # 1. 그래프 구성

    MAP = [list(map(int, input().split())) for _ in range(N)]

    #최단 거리가 저장되는 배열! 
    visited = [[INF] * N for _ in range(N)]
    #2. 큐 생성

    q = deque()

    #3. 시작점 세팅

    start_row = 0
    start_col = 0

    q.append((start_row, start_col))
    visited[start_row][start_col] = 0

    #.4 ~ 7 반복 큐가 빌때가지!

    while q:
    #4 첫번쨰 점 꺼내기
        now_row, now_col = q.popleft()
    #5. next 점 찾기
        dr = [1,-1, 0, 0]
        dc = [0,0, 1,-1]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            #높이차이
            diff = 0
            
            #높이 차이가 나면 그 높이 차이만큼이 가중치
            if MAP[now_row][now_col] < MAP[next_row][next_col]:
                diff = MAP[next_row][next_col] - MAP[now_row][now_col]

            #새롭게 갈 좌표의 최단거리 =  현위치의 최단거리 + diff + 1(기본비용)
            if visited[next_row][next_col] > visited[now_row][now_col] + diff + 1:
                visited[next_row][next_col] = visited[now_row][now_col] + diff + 1
                q.append((next_row, next_col))

    print(f"#{tc} {visited[N-1][N-1]}")















