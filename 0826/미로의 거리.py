

'''

값 찾는거 방법 3가지,,!

1, now에서 꺼냇을대

2. next에 큐 추가할때

3. 다 끝나고 한번에 !


'''
from collections import deque

T = int(input())


for tc in range(1, T+1):


    N = int(input())

    #1. 연결구조를 구성
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)] #이건 2차원 맵형태로 받아서 +1 안하는 것!
    result = 0

    #2. queue 생성
    q = deque()

    #3. 시작점 세팅


    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                visited[row][col] = 1
                q.append([row, col])

    while len(q) and result == 0 : #큐에 값이 있는 동안
        #4 큐에서 맨 앞점을 꺼냄

        now = q.popleft()
        now_row = now[0]
        now_col = now[1]

        if MAP[now_row][now_col] == 3:
            result += 1
            res_row = now_row
            res_col = now_col


        #5. now에서 갈 수 있는 모든 점을 찾기(next)

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row <0 or next_col < 0 or next_row >= N or next_col >= N:
                continue

            if MAP[next_row][next_col] == 1:
                continue

            # #값을 찾았다!
            # if visited[next_row][next_col] == 3:
            #     result = 1
            #     break

            #6 next를 큐에 넣기
            visited[next_row][next_col] = visited[now_row][now_col] + 1

            q.append([next_row, next_col])

    if result == 0 :
        print("#{} {}".format(tc, result))
    else:
        ans = visited[res_row][res_col] - 2
        print("#{} {}".format(tc, ans))



#######


from collections import deque

T = int(input())

for tc in range(T):
    N = int(input())
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]
    # 1. 그래프 구성

    # 2. queue생성
    q = deque()
    visited = [[0]* N for _ in range(N)]

    # 3. 시작점 세팅
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                visited[row][col] = 1
                q.append([row, col])
    ans = -1
    # 7. 4~6단계 반복
    while q and ans == -1:
        # 4. now꺼내기
        now = q.popleft()
        now_row = now[0]
        now_col = now[1]
        # if MAP[now_row][now_col] == 3:
        #     ans = visited[now_row][now_col]
        #     break


        # 5. now -> next찾기
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_col >= N or next_row >= N:
                continue #맵을 벗어나면 무시
            if MAP[next_row][next_col] == 1:
                continue #벽이면 무시
            if visited[next_row][next_col] != 0:
                continue # 찾았던 점이면 무시

            #6. next를 queue추가
            visited[next_row][next_col] = visited[now_row][now_col] + 1
            q.append([next_row, next_col])
            # if MAP[next_row][next_col] == 3:
            #     ans = visited[next_row][next_col] - 2
    #
    # ans = -1
    # for row in range(N):
    #     for col in range(N):
    #         if MAP[row][col] == 3:
    #             ans = visited[row][col] - 2

    if ans < 0:
        print("#{} 0".format(tc + 1))
    else :
        print("#{} {}".format(tc + 1, ans))
