#
# def ADD(value):
#
#     global end
#     q[end] = value
#     end += 1
#     end %= len(q)
#
# def POP():
#     global front
#     global end
#     if front == end:
#         return "error"
#
#     temp = q[front]
#     front += 1
#     front %= len(q)
#     return temp
#
#
#
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#
#
#     N, M = map(int, input().split()) #왜 2개는 입력 잘 받으면서,,!
#     q = list(map(int, input().split())) + [0]
#
#     front = 0
#     end = len(q) - 1
#
#
#     for _ in range(M):
#         temp = POP()
#         ADD(temp)
#
#     print("#{} {}".format(tc, POP()))



'''

1. 연결 구조를 구성
2. queue 생성
3. 시작점 세팅

------준비------
4.queue에서 맨 앞점을 꺼냄(now)
5. now에서 갈 수 있는 모든 점을 찾기(next)
6. next를 queue에 넣기
7. 4~6단계를 queue가 비월질 떄까지




'''
T = int(input())

for tc in range(1, T+1):

    N = int(input())

    #1. 연결 구조를 구성
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]
    visted = [[0] * N for _ in range(N)]


    # 2. queue 생성(append, popghkfdyd version)
    q = []

    #3 시작점 세팅( 시작점으 queue에 추가)

    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                #시작점도 찾은거나 다름없으니 기록
                visted[row][col] == 1
                q.append([row, col])


    while len(q) != 0: #큐에 값이 있는 동안 => 큐가 빌때까지!
        #4. queue에서 맨 앞 점을 꺼냄(now)

        now = q.pop(0)
        now_row = now[0]
        now_col = now[1]

        #5. now에서 갈 수 있는 모든 점을 찾기(next)

        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #안되는 것 검사,,!

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if MAP[next_row][next_col] == 1:
                continue
            if visted[next_row][next_col] != 0:
                continue
            visted[next_row][next_col] = 1

            q.append([next_row, next_col])



