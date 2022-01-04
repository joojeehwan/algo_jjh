'''


1. 연결 구조를 구성

2.queue 생성

3.시작점 세팅.

----준비----

4. 큐에서맨 앞 점을 꺼냄(now)
5. now에서 갈 수 있는 모든 점을 찾기(next)
6. next를 큐에 넣기
7. 4 ~ 6 단계를 큐가 비워질 떄까지,,,!



옵션 :

1.맵을 벗어나는가?! : 2차원맵 한정
2. 갈 수 없는 점 확인
3. 갔던 점을 다시 돌아갈 수 있는가?! < viseted배열 활용


'''


T = int(input())


for tc in range(1, T+1):

    N = int(input())

    #1 연결구조를 구성
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    result = 0

    # queue 생서(append, pop활용)
    q = []


    #3 시작점 세팅(시작점을 queue에 추가)
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                visited[row][col] = 1
                q.append([row, col]) #값 이렇게 넣는거,,!!
                                        #튜플의 형태로 q에 하나씩 넣는다!



    while len(q) != 0 and result == 0 : #큐에 값이 있는 동안
        now = q.pop(0)
        now_row = now[0]
        now_col = now[1]
        
        
        #상 하 좌 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]


        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #안되는 것 검사
            if next_row < 0 or next_col< 0 or next_row >= N or next_col >= N:
                continue # 맵 나가는 것!

            if MAP[next_row][next_col] == 1:
                continue

            if visited[next_row][next_col] != 0 :
                continue

            if MAP[next_row][next_col] == 3:
                result = 1
                break

            visited[next_row][next_col] = 1
            q.append([next_row, next_col])

    print("{} {}".format(tc , result))

       

